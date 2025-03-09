with open('chn_ip.txt', 'r') as f:
    lines = f.readlines()
with open('chn_ip_loon.txt', 'w') as f:
    for line in lines:
        if line.strip():  # 忽略空行
            f.write(f'IP-CIDR,{line.strip()},DIRECT\n')
