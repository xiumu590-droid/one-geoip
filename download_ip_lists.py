import os
import requests

def download_file(url, output_file):
    """下载文件并保存到指定路径"""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        with open(output_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"成功下载: {url} -> {output_file}")
        return True
    except Exception as e:
        print(f"下载失败: {url}, 错误: {e}")
        return False

def main():
    os.makedirs("temp", exist_ok=True)

    # URL 列表
    cn_url        = "https://china-operator-ip.yfgao.com/china46.txt"
    cn_dx_url     = "https://china-operator-ip.yfgao.com/chinanet46.txt"
    cn_yd_url     = "https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists/cmcc46.txt"
    cn_lt_url     = "https://china-operator-ip.yfgao.com/unicom46.txt"
    cn_jy_url     = "https://china-operator-ip.yfgao.com/cernet46.txt"
    cn_kj_url     = "https://china-operator-ip.yfgao.com/cstnet46.txt"
    cn_pbs_url    = "https://china-operator-ip.yfgao.com/drpeng46.txt"

    # 本地文件
    ip_cn_file  = "temp/1.txt"
    ip_dx_file  = "temp/2.txt"
    ip_lt_file  = "temp/3.txt"
    ip_jy_file  = "temp/4.txt"
    ip_kj_file  = "temp/5.txt"
    ip_pbs_file = "temp/6.txt"
    ip_yd_file  = "temp/8.txt"

    output_file = "china.txt"

    # 下载
    download_file(cn_url, ip_cn_file)
    download_file(cn_dx_url, ip_dx_file)
    download_file(cn_yd_url, ip_yd_file)
    download_file(cn_lt_url, ip_lt_file)
    download_file(cn_jy_url, ip_jy_file)
    download_file(cn_kj_url, ip_kj_file)
    download_file(cn_pbs_url, ip_pbs_file)

    # 合并
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for infile in [
            ip_cn_file, ip_dx_file, ip_lt_file, ip_jy_file,
            ip_kj_file, ip_pbs_file, ip_yd_file
        ]:
            if not os.path.exists(infile):
                continue

            with open(infile, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        outfile.write(line + "\n")

    print(f"已合并 IP 列表到 {output_file}")

if __name__ == "__main__":
    main()
