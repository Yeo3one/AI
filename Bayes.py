from pandas import DataFrame

# P(A1) + P(A2) = 1
a1 = 0.7  # P(A1)
a2 = 0.3  # P(A2)

b_a1 = 0.2  # P(B|A1)
b_a2 = 0.9  # P(B|A2)

# 결합확률
hap_a1_b = a1 * b_a1
hap_a2_b = a2 * b_a2

p_b = hap_a1_b + hap_a2_b

# 사후확률
sahoo_a1 = hap_a1_b / p_b
sahoo_a2 = hap_a2_b / p_b

bayes = DataFrame({
    "사건": ['A1', 'A2'],
    '사전확률_P(AI)': [a1, a2],
    '조건부확률_P(B|AI)': [b_a1, b_a2],
    '결합확률_P(AI*B)': [hap_a1_b, hap_a2_b],
    '사후확률_P(AI|B)': [sahoo_a1, sahoo_a2]
})

bayes
