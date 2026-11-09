import requests
import json



class Domain:
    def __init__(self, email, key, secret):
        self.email = email
        self.key = key
        self.secret = secret
        self.api="https://api005.dnshe.com/index.php?m=domain_hub&endpoint=subdomains&action=%s"
    def get_domains(self):
        response = requests.get(
            self.api % "list",
            headers={
                "X-API-Key": self.key,
                "X-API-Secret": self.secret
                },
            timeout=30,
        )
        result = response.json()
        # return result
        if result["success"]:
            domains ={}
            for item in result["subdomains"]:
                domain_id=item["id"]
                domain=item["full_domain"]
                expires_at=item["expires_at"]
                domains[domain] = {"id":domain_id,"expires_at":expires_at}
            return {self.email:domains}
        else:
            return result
    def renew(self, domain_id):
        response = requests.post(
            self.api % "renew",
            headers={
                "X-API-Key": self.key,
                "X-API-Secret": self.secret
                },
            json={"subdomain_id": domain_id},
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
        key = token["key"]
        secret = token["secret"]
        
        api = Domain(email, key, secret)
        domains=account[email]
        for domain in domains:
            id=domain[0]
            result = api.renew(id)  
            print(result)
    # 获取更新后的域名列表期时间
    renew_domains=api.get_domains()
    # 更新当前账号下的域名列表期时间
    _account={}
    for email in account:
        _account[email]={}
        for domain in account[email]:
            expires_at=renew_domains[email][domain]["expires_at"]
            expire=expires_at[:10]
            _account[email][domain]={"expires_at":expire}
    # 提交到cloudflare
    response = requests.post(
        "https://dh.str.xx.kg/update-domains",
        json=_account,
        timeout=30,
    )
    result = response.json()
    print(result)
