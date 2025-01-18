import base64

def process_line(line):
    try:
        # แยกเลขบรรทัดกับข้อมูลออกจากกัน
        parts = line.strip().split(':', 1)
        if len(parts) != 2:
            return None
        
        line_number = parts[0]
        data = parts[1]
        
        # เช็คว่าเลขบรรทัดเป็นตัวเลขจริงๆ
        if not line_number.isdigit():
            return None
            
        return int(line_number), data
        
    except Exception as e:
        print(f"Error processing line: {line}")
        return None

def combine_base64_lines(filename):
    lines_data = {}  # เก็บข้อมูลในรูปแบบ {line_number: data}
    
    with open(filename, 'r') as f:
        for line in f:
            result = process_line(line)
            if result:
                line_number, data = result
                lines_data[line_number] = data
    
    # เรียงข้อมูลตามเลขบรรทัด
    combined = ''
    for i in range(max(lines_data.keys()) + 1):
        if i in lines_data:
            combined += lines_data[i]
        else:
            print(f"Warning: Missing line {i}")
    
    return combined

# ใช้งาน
try:
    filename = "outpu.txt"  # ชื่อไฟล์ที่มีข้อมูล base64
    combined_data = combine_base64_lines(filename)
    
    # ลองแปลงเป็น binary
    decoded_data = base64.b64decode(combined_data)
    
    # บันทึกเป็นไฟล์รูป
    with open("output_image.jpg", "wb") as f:
        f.write(decoded_data)
    print("Successfully decoded and saved the image")
    
except Exception as e:
    print(f"Error: {e}")