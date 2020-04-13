import requests


def main():
    term_select_url = "https://es.stevens.edu/ia-bin/tsrvweb.exe?&WID=W&tserve_tip_write=||WID&ConfigName=" \
                      "rcrssecthp1&ReqNum=1&TransactionSource=H&tserve_trans_config=rcrssecthp1.cfg&tserve_" \
                      "host_code=[HostZero]&tserve_tiphost_code=[TipZero]"

    xml = requests.get(term_select_url, allow_redirects=True)

    for line in xml.text.split("\n"):
        print(line)


main()
