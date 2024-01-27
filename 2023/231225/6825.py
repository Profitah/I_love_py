def b(w, h):  # BMI 계산 함수
    return w / (h * h)

def bmi_category(w, h):  # 체질량지수(BMI) 계산 및 결과 출력 함수
    bmi_val = b(w, h)  # BMI 계산
    
    # BMI 범주에 따라 결과 문자열 설정
    result = "Underweight" if bmi_val < 18.5 else "Normal weight" if 18.5 <= bmi_val < 25 else "Overweight"
    
    return result

if __name__ == "__main__":
    w_input = float(input())  # 체중 입력
    h_input = float(input())  # 키 입력
    
    print(bmi_category(w_input, h_input))  # 결과 출력
