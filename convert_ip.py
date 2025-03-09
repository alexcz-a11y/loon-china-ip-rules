import ipaddress

# 处理 IPv4 文件
with open('chn_ip.txt', 'r') as f:
    lines = f.readlines()

with open('chn_ip_loon.txt', 'w') as f:
    for line in lines:
        line = line.strip()
        if line:  # 忽略空行
            try:
                # 假设每行是 "start_ip end_ip" 格式
                start_ip, end_ip = line.split()
                # 将范围转换为 CIDR
                network = ipaddress.summarize_address_range(
                    ipaddress.ip_address(start_ip),
                    ipaddress.ip_address(end_ip)
                )
                # 写入所有 CIDR 格式规则
                for net in network:
                    f.write(f'IP-CIDR,{net},DIRECT\n')
            except ValueError as e:
                print(f"Error processing IPv4 line '{line}': {e}")

# 处理 IPv6 文件
with open('chn_ip_v6.txt', 'r') as f:
    lines = f.readlines()

with open('chn_ip_loon_v6.txt', 'w') as f:
    for line in lines:
        line = line.strip()
        if line:  # 忽略空行
            try:
                # 假设每行是 "start_ip end_ip" 格式
                start_ip, end_ip = line.split()
                # 将范围转换为 IPv6 CIDR
                network = ipaddress.summarize_address_range(
                    ipaddress.ip_address(start_ip),
                    ipaddress.ip_address(end_ip)
                )
                # 写入所有 IPv6 CIDR 格式规则
                for net in network:
                    f.write(f'IP-CIDR6,{net},DIRECT\n')
            except ValueError as e:
                print(f"Error processing IPv6 line '{line}': {e}")
