def generate_readme():
    # Thu thập thông tin từ người dùng
    project_name = input("Nhập tên dự án: ")
    description = input("Nhập mô tả dự án: ")
    author = input("Nhập tên tác giả: ")
    license_type = input("Nhập loại giấy phép (ví dụ: MIT, Apache 2.0): ")

    # Nội dung README
    readme_content = f"""# {project_name}

## Mô tả
{description}

## Cài đặt
```bash
# Hướng dẫn cài đặt sẽ được thêm tại đây
```

## Sử dụng
```bash
# Ví dụ lệnh sử dụng sẽ được thêm tại đây
```

## Tác giả
- {author}

## Giấy phép
This project is licensed under the {license_type} License.
"""

    # Ghi nội dung vào file README.md
    try:
        with open("README.md", "w", encoding="utf-8") as file:
            file.write(readme_content)
        print("File README.md đã được tạo thành công!")
    except Exception as e:
        print(f"Lỗi khi tạo file: {e}")

if __name__ == "__main__":
    generate_readme()