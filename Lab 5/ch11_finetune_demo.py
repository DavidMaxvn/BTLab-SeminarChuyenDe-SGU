import json
from pathlib import Path


def validate_jsonl_file(path: str) -> None:
    """
    Kiểm tra nhanh file JSONL trước khi upload fine-tuning.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Không tìm thấy file: {path}")

    with file_path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Dòng {line_number} không phải JSON hợp lệ: {exc}") from exc

            if "messages" not in obj:
                raise ValueError(f"Dòng {line_number} thiếu key 'messages'.")

            if not isinstance(obj["messages"], list) or len(obj["messages"]) < 2:
                raise ValueError(f"Dòng {line_number} phải có danh sách 'messages' hợp lệ.")

    print(f"File {path} hợp lệ để dùng làm dữ liệu fine-tuning.")


def print_openai_cli_steps() -> None:
    """
    In ra các bước minh họa để đưa vào báo cáo/lab.
    """
    print("=== Các bước fine-tuning minh họa ===")
    print("1. Chuẩn bị file JSONL training data")
    print("2. Kiểm tra file hợp lệ")
    print("3. Upload file lên OpenAI platform")
    print("4. Tạo fine-tuning job")
    print("5. Sau khi job hoàn tất, dùng model fine-tuned trong API call")


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    training_file = script_dir / "ch11_finetune_training.jsonl"
    validate_jsonl_file(str(training_file))
    print_openai_cli_steps()