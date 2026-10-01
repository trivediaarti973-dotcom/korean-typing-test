import random
import time
import unicodedata

sentences = [
    "안녕하세요 만나서 반갑습니다",
    "오늘 날씨가 정말 좋네요",
    "저는 한국어를 공부하고 있습니다",
    "투자 제안서를 검토해 주세요",
]

def count_keystrokes(text):
    return len(unicodedata.normalize("NFD", text.replace(" ", "")))

def accuracy(target, typed):
    matches = sum(a == b for a, b in zip(target, typed))
    return matches / len(target) * 100
rounds = 5
speeds = []
accuracies = []

for i in range(1, rounds + 1):
    target = random.choice(sentences)
    print(f"\n[{i}/{rounds}] 아래 문장을 입력하세요:\n")
    print(target, "\n")

    input("준비되면 Enter를 누르세요...")
    start = time.time()
    typed = input("> ")
    elapsed = time.time() - start

    cpm = count_keystrokes(typed) / elapsed * 60
    acc = accuracy(target, typed)
    speeds.append(cpm)
    accuracies.append(acc)

    print(f"타수: {cpm:.0f} 타/분 | 정확도: {acc:.1f}%")

print("\n===== 최종 결과 =====")
print(f"평균 타수: {sum(speeds) / rounds:.0f} 타/분")
print(f"평균 정확도: {sum(accuracies) / rounds:.1f}%")