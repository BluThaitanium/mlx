from subprocess import PIPE, run

no_vulnerabilities = "found 0 vulnerabilities"


class colorText:
    RED = "\033[1;31m"
    GREEN = "\033[0;32m"
    END = "\033[0;0m"


def audit_npm():
    format_vulnerablility_output = ""
    audit_npm = (
        run("npm audit fix", cwd="./dashboard/origin-mlx/", stdout=PIPE, shell=True)
        .stdout.decode("utf-8")
        .split("\n\n")
    )
    for message in audit_npm:
        format_vulnerablility_output = (
            message
            if "vulnerabilities" in message
            else format_vulnerablility_output
        )
    if no_vulnerabilities not in audit_npm:
        print(
            f"\n\n{colorText.RED}Vulnerabilites still present:\n{format_vulnerablility_output}{colorText.END}"
        )
        print("\nMaual investigation necessary to prevent breaking changes\n\n")
        print(
            f"Run:\n\t{colorText.GREEN}npm audit{colorText.END}\nand scroll up to manually manage breaking changes\n\n"
        )
        print(
            f"Run:\n\t{colorText.GREEN}npm audit fix --force{colorText.END}\nto force update all packages including breaking changes\n\n"
        )
        input("Press any key to continue make check_doc_links ")


def fix_vulnerabilities(output: (bool, bytes)):
    (has_vulnerabilities, update_npm) = output
    continue_audit = False
    format_vulnerablility_output = ""

    if has_vulnerabilities:
        for message in update_npm:
            format_vulnerablility_output = (
                message
                if "vulnerabilities" in message
                else format_vulnerablility_output
            )
        user_input = input(
            f"{colorText.RED}\n\nVulnerabilities found:\n{format_vulnerablility_output}{colorText.END}\n\nWould you like to audit? [y,n]: "
        )
        continue_audit = True if user_input in ["Y", "y"] else False
    if continue_audit:
        audit_npm()


def verify_npm_packages() -> (bool, bytes):
    check_outdated = run("npm outdated", cwd="./dashboard/origin-mlx/", shell=True)
    update_packages = False
    has_vulnerabilities = False
    update_npm = ""

    if check_outdated.returncode == 1:
        user_input = input(
            "\n\nFound outdated npm packages. Would you like to update these packages? [y,n]: "
        )
        update_packages = True if user_input in ["Y", "y"] else False

    if update_packages:
        run(["rm", "package-lock.json"], cwd="./dashboard/origin-mlx/")
        update_npm = run(
            "npm update", cwd="./dashboard/origin-mlx/", stdout=PIPE, shell=True
        ).stdout.decode("utf-8")

        has_vulnerabilities = no_vulnerabilities not in update_npm
    return has_vulnerabilities, update_npm.split("\n\n")


if __name__ == "__main__":
    output = verify_npm_packages()
    fix_vulnerabilities(output)
