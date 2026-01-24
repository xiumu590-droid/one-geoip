import os
import requests

def download_file(url, output_file):
    """下载文件并保存到指定路径"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(output_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"成功下载: {url} -> {output_file}")
        return True
    except Exception as e:
        print(f"下载失败: {url}, 错误: {e}")
        return False

def main():
    # 创建临时目录
    os.makedirs("temp", exist_ok=True)
    
    # 下载列表
    cn_url = "https://gaoyifan.github.io/china-operator-ip/china46.txt"
    cn-dianxin_url = "https://gaoyifan.github.io/china-operator-ip/chinanet46.txt"
    cn-yidong_url = "https://gaoyifan.github.io/china-operator-ip/cmcc46.txt"
    cn-liantong_url = "https://gaoyifan.github.io/china-operator-ip/unicom46.txt"
    cn-jiaoyu_url = "https://gaoyifan.github.io/china-operator-ip/cernet46.txt"
    cn-keji_url = "https://gaoyifan.github.io/china-operator-ip/cstnet46.txt"
    cn-pengboshi_url = "https://gaoyifan.github.io/china-operator-ip/drpeng46.txt"
    cn-google_url = "https://gaoyifan.github.io/china-operator-ip/googlecn46.txt"
    
    ip-cn_file = "temp/1.txt"
    ip-dx_file = "temp/2.txt"
    ip-lt_file = "temp/3.txt"
    ip-jy_file = "temp/4.txt"
    ip-kj_file = "temp/5.txt"
    ip-pbs_file = "temp/6.txt"
    ip-gg_file = "temp/7.txt"
    ip-yd_file = "temp/8.txt"
    output_file = "china.txt"
    
    # 下载文件
    download_file(cn_url, ip-cn_file)
    download_file(cn-dianxin_url, ip-dx_file)
    download_file(cn-yidong_url, ip-yd_file)
    download_file(cn-liantong_url, ip-lt_file)
    download_file(cn-jiaoyu_url, ip-jy_file)
    download_file(cn-keji_url, ip-kj_file)
    download_file(cn-pengboshi_url, ip-pbs_file)
    download_file(cn-google_url, ip-gg_file)
    # 合并文件
    with open(output_file, 'w') as outfile:
        for infile in [ipv4_file, ipv6_file]:
            try:
                with open(infile, 'r') as f:
                    for line in f:
                        # 去掉首尾空格
                        cleaned_line = line.strip()
                        if cleaned_line:
                            outfile.write(f"{cleaned_line}\n")
            except Exception as e:
                print(f"处理文件 {infile} 时出错: {e}")
    
    print(f"已合并IP列表到 {output_file}")

if __name__ == "__main__":
    main()
