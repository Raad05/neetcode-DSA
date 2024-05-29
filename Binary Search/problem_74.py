class Solution(object):
    def searchMatrix(self, matrix, target):
        m_lo, m_hi = 0, len(matrix) - 1

        while m_lo <= m_hi:
            m_mid = (m_lo + m_hi) // 2

            if matrix[m_mid][0] > target:
                m_hi = m_mid - 1
            elif matrix[m_mid][0] < target:
                n_lo, n_hi = 0, len(matrix[m_mid]) - 1

                while n_lo <= n_hi:
                    n_mid = (n_lo + n_hi) // 2

                    if matrix[m_mid][n_mid] > target:
                        n_hi = n_mid - 1
                    elif matrix[m_mid][n_mid] < target:
                        n_lo = n_mid + 1
                    else:
                        return True
                    
                m_lo = m_mid + 1
            else:
                return True

        return False
        