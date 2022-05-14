import os
import requests
import wget
import typer

typer.secho("Welcome to website screenshot and domain checker 🚀", fg=typer.colors.BRIGHT_MAGENTA, bold=True)
options = ['Domain Checker', 'Screenshot']

op_sec = typer.prompt("⚡Domain Checker/⚡Screenshot")

if op_sec == options[0]:
    domain_Name = typer.prompt("Domain Name")
    r = requests.get(f"https://domain-availability.whoisxmlapi.com/api/v1?apiKey=at_0HgAQ09RqstrKcRdWoagXiGOYJeZj&domainName={domain_Name}&credits=DA")
    t = r.json()
    if t['DomainInfo']['domainAvailability'] == "AVAILABLE":
        typer.secho("Domain Avialable 🔥",fg=typer.colors.MAGENTA)

    else:
        typer.secho("Domain Not Avialable 😒",fg=typer.colors.MAGENTA)

else:
    try:

        domain = typer.prompt("Domain Name")

        file_name = typer.prompt("File Name to save screenshot in 📁") + '.png'

        r = f"https://api.apiflash.com/v1/urltoimage?access_key=d9bdb788d78847038537b7b0bed4f066&wait_until=page_loaded&url=https://{domain}&no_ads=false&fresh=true&format=png"

        wget.download(r, file_name)

        typer.secho("\nScreenshot is saved at:", fg=typer.colors.BRIGHT_RED)

        file_path = os.getcwd() + "/" + file_name

        typer.secho(file_path, fg=typer.colors.BRIGHT_RED)

    except:
        typer.secho("Domain Name Not Found 😒", fg=typer.colors.BRIGHT_GREEN)