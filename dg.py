import requests
import os
import json



class Domain:
    def __init__(self, email, token):
        self.email = email
        self.token = token
        self.api="https://domain-api.digitalplat.org/api/v1/domains"
    def get_domains(self):
        response = requests.get(
            self.api,
            headers={"Authorization": f"Bearer {self.token}"},
            timeout=30,
        )
        result = response.json()
        if result["success"]:
            domains ={}
            for item in result["data"]:
                domain=item["domain"]
                expires_at=item["expires_at"]
                domains[domain] = expires_at
            return domains
        else:
            return result
    def renew(self, domain):
        response = requests.request(
            "POST",
            f"{self.api}/{domain}/renew",
            headers={"Authorization": f"Bearer {self.token}"},
            json={"years": 1, "payment_method": "sandbox"},
            timeout=30,
        )
        result = response.json()
        return result


if __name__ == "__main__":
    account=json.loads(os.environ["ACCOUNTS"])
    tokens=json.loads(os.environ["TOKENS"])
    # 续费当前账号下的所有域名并更新过期时间
    for email in account:
        token = tokens[email]
        api = Domain(email, token)
        domains=account[email]
        for domain in domains:
            result = api.renew(domain)  
            print(result)
    # 获取更新后的域名列表期时间
    renew_domains=api.get_domains()
    # 更新当前账号下的域名列表期时间
    _account={}
    for email in account:
        _account[email]={}
        for domain in account[email]:
            expires_at=renew_domains[domain]
            expire=f"{expires_at[0:4]}-{expires_at[5:7]}-{expires_at[8:10]}"
            _account[email][domain]=expire
    # 提交到cloudflare
    response = requests.post(
        "https://dg.str.xx.kg/update-domains",
        json=_account,
        timeout=30,
    )
    result = response.json()
    print(result)
    # 写入文件
