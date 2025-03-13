import PyPDF2
import os
import time
import re

def clean_text(text):
    """
    清理文本，移除不可打印字符和处理编码问题
    """
    if text is None:
        return ""
    
    # 替换不可打印字符
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]', '', text)
    
    # 处理常见的编码问题
    text = text.replace('\ufeff', '')  # 移除BOM
    
    return text

def extract_pdf_in_batches(pdf_path, output_dir, batch_size=5):
    """
    分批处理PDF文件，每批处理batch_size页，并将结果保存到单独的文件中
    
    Args:
        pdf_path: PDF文件路径
        output_dir: 输出目录
        batch_size: 每批处理的页数
    """
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        # 打开PDF文件
        pdf = PyPDF2.PdfReader(pdf_path)
        total_pages = len(pdf.pages)
        print(f"PDF文件共有 {total_pages} 页")
        
        # 计算需要处理的批次数
        num_batches = (total_pages + batch_size - 1) // batch_size
        
        # 分批处理
        for batch in range(num_batches):
            start_page = batch * batch_size
            end_page = min((batch + 1) * batch_size, total_pages)
            
            print(f"处理批次 {batch+1}/{num_batches}，页码 {start_page+1} 到 {end_page}")
            
            # 提取当前批次的文本
            batch_text = ""
            for i in range(start_page, end_page):
                print(f"  提取页面 {i+1}/{total_pages}...")
                try:
                    text = pdf.pages[i].extract_text()
                    # 清理文本
                    text = clean_text(text)
                    batch_text += f"--- 第 {i+1} 页 ---\n{text}\n\n"
                except Exception as e:
                    print(f"  提取页面 {i+1} 时出错: {e}")
                    batch_text += f"--- 第 {i+1} 页 ---\n[提取错误]\n\n"
            
            # 保存当前批次的文本
            output_file = os.path.join(output_dir, f"agents_pdf_batch_{batch+1:03d}.txt")
            try:
                with open(output_file, "w", encoding="utf-8", errors="replace") as f:
                    f.write(batch_text)
                print(f"  批次 {batch+1} 已保存到 {output_file}")
            except Exception as e:
                print(f"  保存批次 {batch+1} 时出错: {e}")
            
            # 短暂暂停，避免系统资源过度使用
            time.sleep(0.5)
        
        # 创建一个索引文件，列出所有批次文件
        index_file = os.path.join(output_dir, "agents_pdf_index.txt")
        with open(index_file, "w", encoding="utf-8", errors="replace") as f:
            f.write(f"PDF文件: {os.path.basename(pdf_path)}\n")
            f.write(f"总页数: {total_pages}\n")
            f.write(f"批次大小: {batch_size}\n")
            f.write(f"总批次数: {num_batches}\n\n")
            f.write("批次文件列表:\n")
            for batch in range(num_batches):
                f.write(f"  - agents_pdf_batch_{batch+1:03d}.txt (页码 {batch*batch_size+1} 到 {min((batch+1)*batch_size, total_pages)})\n")
        
        print(f"\n处理完成！索引文件已保存到 {index_file}")
        return True
    
    except Exception as e:
        print(f"处理PDF时出错: {e}")
        return False

def combine_batch_files(output_dir, combined_file):
    """
    将所有批次文件合并为一个文件
    
    Args:
        output_dir: 包含批次文件的目录
        combined_file: 合并后的文件路径
    """
    try:
        # 获取所有批次文件
        batch_files = [f for f in os.listdir(output_dir) if f.startswith("agents_pdf_batch_") and f.endswith(".txt")]
        batch_files.sort()
        
        # 合并文件
        with open(combined_file, "w", encoding="utf-8", errors="replace") as outfile:
            for batch_file in batch_files:
                file_path = os.path.join(output_dir, batch_file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="replace") as infile:
                        outfile.write(infile.read())
                    outfile.write("\n\n")
                except Exception as e:
                    print(f"读取文件 {batch_file} 时出错: {e}")
                    outfile.write(f"[读取文件 {batch_file} 时出错]\n\n")
        
        print(f"所有批次文件已合并到 {combined_file}")
        return True
    
    except Exception as e:
        print(f"合并文件时出错: {e}")
        return False

if __name__ == "__main__":
    # 获取当前目录
    current_dir = os.getcwd()
    print(f"当前目录: {current_dir}")
    
    # 设置输入和输出路径
    input_dir = os.path.join(current_dir, "input")
    output_dir = os.path.join(current_dir, "output", "agents_pdf")
    
    # 查找PDF文件
    pdf_file = None
    for file in os.listdir(input_dir):
        if "Building effective agents" in file and file.endswith(".pdf"):
            pdf_file = file
            break
    
    if pdf_file:
        pdf_path = os.path.join(input_dir, pdf_file)
        print(f"找到PDF文件: {pdf_path}")
        
        # 分批处理PDF
        success = extract_pdf_in_batches(pdf_path, output_dir, batch_size=5)
        
        if success:
            # 合并所有批次文件
            combined_file = os.path.join(current_dir, "agents_pdf_content.txt")
            combine_batch_files(output_dir, combined_file)
    else:
        print("未找到匹配的PDF文件") 