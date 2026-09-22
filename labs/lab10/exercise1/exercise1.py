num_rounds = int(input())
#initialize
rounds_processed = num_rounds
final_score = 0

for i in range (num_rounds):
    score = float(input())
    if score > 100:
        score += score * 0.2
    final_score += score

print(f"{final_score:.1f}")
print(rounds_processed)
