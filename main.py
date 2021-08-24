from fastapi import FastAPI
import whois

app = FastAPI()


@app.get("/simple/{domain}", tags=["domain"])
def domaininfofinder(domain: str):
    """
    Simply returns the results
    """
    result = whois.whois(domain)
    return result


@app.get("/{domain}", tags=["domain"])
def domaininfofinder(domain: str):
    """
    Returns the processed results
    If some field is null, custom message is show i.e, "Not Available"
    """
    result = whois.whois(domain)

    res = {
        # Domain name:
        "domain_name": result.domain_name,

        # 1. Registration and Expiry Date:
        "registration_date" : "Registration: " + str(null_checker(result.creation_date)),
        
        "expiry_date": "Expiry: " + str(null_checker(result.expiration_date)),

        # 2. Website Owner Details:
        "org": "Organization: " + str(null_checker(result.org)),
        "address": "Address: " + str(null_checker(result.address)),
        "registrar": "Registar: " + str(null_checker(result.registrar)),
        "emails": "Contact Email: " + str(null_checker(result.emails)),

        # Website Nameservers:
        "name_servers": null_checker(result.name_servers),

        # Other Details:
        "updated_date": "Updated Date: " + str(null_checker(result.updated_date)),
        "country": null_checker(result.country),
        "city": null_checker(result.city),
        "state": null_checker(result.state),
        "zipcode": null_checker(result.zipcode),
        "dnssec": null_checker(result.dnssec),
        "name": null_checker(result.name)

    }
    null_checker(null_checker(result.state))
    
    return res


def null_checker(res):
    """
    This function will check wheter the field is null or not.
    If it's null, Custom message is returned.
    """
    if res is None:
        return "Not Available"
    return res
