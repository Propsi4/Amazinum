def coin_probabilities(coin_results, coins_probabilities):
    # Initialize hypotheses probabilities
    hypotheses = [1/len(coins_probabilities)] * len(coins_probabilities)
    probabilities = []
    
    # Calculate initial probability of H side
    p_h = sum([hypotheses[i] * coins_probabilities[i] for i, _ in enumerate(coins_probabilities)]) # = 0.48

    for result in coin_results:
        if result == 'H':
            # Update hypotheses probabilities using Bayes formula
            for i, _ in enumerate(hypotheses):
                hypotheses[i] = (coins_probabilities[i] * hypotheses[i]) / p_h
        else:
            # Update hypotheses probabilities using Bayes formula
            for i, _ in enumerate(hypotheses):
                hypotheses[i] = ((1 - coins_probabilities[i]) * hypotheses[i]) / (1 - p_h)
        
        # Calculate new probability of H side
        p_h = sum([hypotheses[i] * coins_probabilities[i] for i, _ in enumerate(coins_probabilities)])
        probabilities.append(p_h)
    
    return probabilities


coin_results = ['H', 'H', 'H', 'T', 'H', 'T', 'H', 'H']
coins_probabilities = [0.1, 0.2, 0.4, 0.8, 0.9]
probabilities = coin_probabilities(coin_results, coins_probabilities)
print([round(probabilities[i], 2) for i, _ in enumerate(probabilities)])

# answer is [0.69, 0.79, 0.83, 0.74, 0.8, 0.69, 0.76, 0.8]