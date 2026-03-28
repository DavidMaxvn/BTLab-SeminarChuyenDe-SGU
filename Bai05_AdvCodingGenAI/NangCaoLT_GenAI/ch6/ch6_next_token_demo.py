from collections import defaultdict, Counter
import random


class BigramCharModel:
    """
    Mô hình bigram ký tự đơn giản:
    học xác suất ký tự tiếp theo dựa trên ký tự hiện tại.
    """

    def __init__(self) -> None:
        self.transitions: dict[str, Counter] = defaultdict(Counter)

    def fit(self, text: str) -> None:
        normalized = text.lower()
        for i in range(len(normalized) - 1):
            current_char = normalized[i]
            next_char = normalized[i + 1]
            self.transitions[current_char][next_char] += 1

    def predict_next_char(self, current_char: str) -> str:
        current_char = current_char.lower()
        if current_char not in self.transitions:
            return " "

        counter = self.transitions[current_char]
        chars = list(counter.keys())
        weights = list(counter.values())
        return random.choices(chars, weights=weights, k=1)[0]

    def generate_text(self, start_char: str, length: int = 100) -> str:
        result = [start_char]
        current_char = start_char

        for _ in range(length - 1):
            next_char = self.predict_next_char(current_char)
            result.append(next_char)
            current_char = next_char

        return "".join(result)


if __name__ == "__main__":
    sample_corpus = """
    large language models predict the next token based on context.
    chatgpt and copilot are built on top of llm technologies.
    prompt engineering improves the quality of generated outputs.
    """

    model = BigramCharModel()
    model.fit(sample_corpus)

    print("=== Demo dự đoán ký tự tiếp theo ===")
    for ch in ["l", "p", "c", "o"]:
        print(f"Ký tự sau '{ch}' có thể là: {model.predict_next_char(ch)}")

    print("\n=== Sinh chuỗi thử nghiệm ===")
    generated = model.generate_text(start_char="l", length=120)
    print(generated)