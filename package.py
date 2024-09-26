name = "rv"

version = "2024.1.0"

authors = [
    "Autodesk"
]

description = \
    """
    Digital review tool for animation, VFX, and game development.
    """

tools = [
    "rv",
    "rvio",
]

requires = [
    "ocio_config"
]

uuid = "autodesk.rv"

build_command = ""


def commands():

    match system.platform:
        case "windows":
            env.RV_INSTALL_PATH = f"C:\\PROGRA~1\\Autodesk\\RV-{version}"
        case _:
            pass

    executables = {
        "windows": {
            "rv": "rv.exe",
            "rvio": "rvio.exe",
            "rvls": "rvls.exe",
            "rvpkg": "rvpkg.exe",
            "rvprof": "rvprof.exe",
            "rvpush": "rvpush.exe",
            "rvshell": "rvshell.exe",
        },
        "osx": {},
        "linux": {},
    }

    for exec_command, executable_file in executables.get(system.platform).items():
        alias(exec_command, f"{env.RV_INSTALL_PATH}/bin/{executable_file}")
