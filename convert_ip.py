with open('chn_ip.txt', 'r') as f:
    lines = f.readlines()
with open('chn_ip_loon.txt', 'w') as f:
    for line in lines:
        if line.strip():  # 忽略空行
            # 假设 chn_ip.txt 已经是 CIDR 格式，如 1.0.1.0/24
            f.write(f'IP-CIDR,{line.strip()},DIRECT\n')
