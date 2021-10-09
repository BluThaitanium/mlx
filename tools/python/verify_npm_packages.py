from subprocess import PIPE, run

no_vulnerabilities = "found 0 vulnerabilities"

def fix_vulnerabilities(output: (bool, bytes)):
    (has_vulnerabilities, update_npm) = output
    audit_npm = False
    format_vulnerablility_output= ""

    if has_vulnerabilities:
        for message in update_npm:
            format_vulnerablility_output = message if "vulnerabilities" in message else format_vulnerablility_output
        user_input = input(f"\n\nVulnerabilities found:\n{format_vulnerablility_output}\n\nWould you like to audit? [y,n]: ")
        audit_npm = True if user_input in ["Y", "y"] else False

    if audit_npm:
        audit_npm = run("npm audit fix", cwd="./dashboard/origin-mlx/", stdout=PIPE, shell=True).stdout.decode('utf-8').split("\n\n")
        for message in audit_npm:
            format_vulnerablility_output = message if "vulnerabilities" in message else format_vulnerablility_output
        if no_vulnerabilities not in audit_npm:
            print(f"\n\nVulnerabilites still present:\n{format_vulnerablility_output}")
            print("\nMaual investigation necessary to prevent breaking changes\n\n")
            print("Run:\n\tnpm audit\nand scroll up to manually manage breaking changes")
            print("Run:\n\tnpm audit fix --force\nto force update all packages including breaking changes")


def verify_npm_packages() -> (bool, bytes):
    check_outdated = run("npm outdated", cwd="./dashboard/origin-mlx/", shell=True)
    update_packages = False
    has_vulnerabilities = False
    update_npm = False

    if check_outdated.returncode == 1:
        user_input = input(
            "\n\nFound outdated npm packages. Would you like to update these packages? [y,n]: "
        )
        update_packages = True if user_input in ["Y", "y"] else False

    if update_packages:
        run(["rm", "package-lock.json"],  cwd="./dashboard/origin-mlx/")
        update_npm = run("npm update", cwd="./dashboard/origin-mlx/", stdout=PIPE, shell=True).stdout.decode('utf-8')
        has_vulnerabilities = no_vulnerabilities not in update_npm
    return has_vulnerabilities, update_npm.split("\n\n")


if __name__ == "__main__":
    output = verify_npm_packages()
    fix_vulnerabilities(output)
