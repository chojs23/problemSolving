def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    bridgeSum = 0

    while len(trucks_on_bridge):
        answer += 1
        bridgeSum -= trucks_on_bridge.pop(0)
        if truck_weights:
            if bridgeSum + truck_weights[0] <= weight:
                temp = truck_weights.pop(0)
                trucks_on_bridge.append(temp)
                bridgeSum += temp
            else:
                trucks_on_bridge.append(0)
    return answer
