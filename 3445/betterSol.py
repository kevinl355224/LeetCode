def maxDiff(s: str, k: int) -> int:
    n = len(s)
    max_diff = 0

    # Try all 25 combinations of (a, b) where a != b and a, b ∈ {0, 1, 2, 3, 4}
    for char_a in range(5):
        for char_b in range(5):
            if char_a == char_b:
                continue  # skip same-character pairs

            # Initialize prefix arrays
            prefix_diff = [0] * (n + 1)       # difference of counts (a - b)
            prefix_parity = [0] * (n + 1)     # parity of a's count (0=even, 1=odd)
            prefix_b_count = [0] * (n + 1)    # count of b

            # Precompute prefix info
            for i in range(n):
                prefix_diff[i + 1] = prefix_diff[i]
                prefix_parity[i + 1] = prefix_parity[i]
                prefix_b_count[i + 1] = prefix_b_count[i]

                num = int(s[i])
                if num == char_a:
                    prefix_diff[i + 1] += 1
                    prefix_parity[i + 1] ^= 1  # flip parity
                elif num == char_b:
                    prefix_diff[i + 1] -= 1
                    prefix_b_count[i + 1] += 1

            # Initialize 4 groups: each combination of (a_parity, b_count % 2)
            count_b_groups = [[] for _ in range(4)]       # stores prefix_b_count[i]
            min_diff_prefixes = [[] for _ in range(4)]    # stores min prefix_diff[i]
            read_pointer = [0] * 4                        # pointer to valid prefix_b_count[i]

            # Slide window ending at j
            for j in range(k, n + 1):
                i = j - k

                # Classify index i into group by (parity, b_count % 2)
                group_index = (prefix_parity[i] << 1) | (prefix_b_count[i] & 1)

                # Store b_count[i] into the corresponding group
                prev_diff = prefix_diff[i]
                prev_min_diff_list = min_diff_prefixes[group_index]

                # Maintain monotonic min stack for prefix_diff[i]
                if not prev_min_diff_list:
                    prev_min_diff_list.append(prev_diff)
                else:
                    prev_min_diff_list.append(min(prev_diff, prev_min_diff_list[-1]))

                count_b_groups[group_index].append(prefix_b_count[i])

                # Compute the target group to find matching i's
                # We want a parity flip (odd <-> even), so use XOR
                # Keep b_count parity same
                target_group = ((prefix_parity[j] ^ 1) << 1) | (prefix_b_count[j] & 1)

                # We require: prefix_b_count[j] - prefix_b_count[i] ≥ 2
                max_b = prefix_b_count[j] - 2

                cb_list = count_b_groups[target_group]
                min_d_list = min_diff_prefixes[target_group]
                p = read_pointer[target_group]

                # Move read pointer to only valid prefix_b_count[i] ≤ max_b
                while p < len(cb_list) and cb_list[p] <= max_b:
                    p += 1
                read_pointer[target_group] = p

                # If there is at least one valid i, calculate max difference
                if p > 0:
                    min_d = min_d_list[p - 1]
                    max_diff = max(max_diff, prefix_diff[j] - min_d)

    return max_diff
