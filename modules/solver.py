from capsolver_python   import HCaptchaTask
from capmonster_python  import HCaptchaTask
from yaml               import safe_load

config = safe_load(open("config.yml"))
api_key = config["captcha"]["api_key"]
service = config["captcha"]["service"]
site_key = config["captcha"]["site_key"]
site_url = "https://discord.com/"

def solve_captcha():
    if service == "capsolver.com":
        capsolver = HCaptchaTask(api_key)
        task_id = capsolver.create_task(site_key, site_key)
        result = capsolver.join_task_result(task_id)
        token = result.get("gRecaptchaResponse")
        return token
    elif service == "capmonster.cloud":
        capmonster = HCaptchaTask(api_key)
        task_id = capmonster.create_task(site_key, site_key)
        result = capmonster.join_task_result(task_id)
        token = result.get("gRecaptchaResponse")
        return token
    else:
        return None