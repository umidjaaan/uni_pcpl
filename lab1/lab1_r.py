import sys
import math

class BiquadraticEquation:
    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.roots = []

    def get_valid_float(self, prompt):
        while True:
            try:
                value = input(prompt)
                return float(value)
            except ValueError:
                print("Ошибка! Введите корректное число.")

    def get_coef(self, index, prompt):
        if len(sys.argv) > index:
            try:
                coef = float(sys.argv[index])
                print(f"Коэффициент из командной строки: {coef}")
                return coef
            except ValueError:
                print(f"Некорректный коэффициент в командной строке. {prompt}")

        return self.get_valid_float(prompt)

    def get_coefficients(self):
        print("Решение биквадратного уравнения: Ax⁴ + Bx² + C = 0")
        print("=" * 50)

        self.coef_A = self.get_coef(1, "Введите коэффициент A: ")
        self.coef_B = self.get_coef(2, "Введите коэффициент B: ")
        self.coef_C = self.get_coef(3, "Введите коэффициент C: ")

        print(f"\nУравнение: {self.coef_A}x⁴ + {self.coef_B}x² + {self.coef_C} = 0")

    def solve(self):
        a, b, c = self.coef_A, self.coef_B, self.coef_C
        self.roots = []

        if a == 0:
            if b == 0:
                if c == 0:
                    print("Уравнение имеет бесконечное количество решений")
                    return
                else:
                    print("Уравнение не имеет решений")
                    return
            else:
                if -c / b >= 0:
                    t = -c / b
                    root = math.sqrt(t)
                    self.roots.extend([root, -root])
                return

        discriminant = b * b - 4 * a * c

        print(f"Дискриминант квадратного уравнения: {discriminant}")

        if discriminant < 0:
            print("Действительных корней нет")
            return

        t1 = (-b + math.sqrt(discriminant)) / (2 * a)
        t2 = (-b - math.sqrt(discriminant)) / (2 * a)

        print(f"Корни для t=x²: t1 = {t1:.4f}, t2 = {t2:.4f}")

        roots_found = []

        if t1 >= 0:
            root1 = math.sqrt(t1)
            root2 = -math.sqrt(t1)
            roots_found.extend([root1, root2])
            print(f"Из t1 = {t1:.4f} найдены корни: {root1:.4f}, {root2:.4f}")

        if t2 >= 0 and t2 != t1:
            root3 = math.sqrt(t2)
            root4 = -math.sqrt(t2)
            roots_found.extend([root3, root4])
            print(f"Из t2 = {t2:.4f} найдены корни: {root3:.4f}, {root4:.4f}")

        self.roots = sorted(set(roots_found))

    def print_solution(self):
        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТЫ РЕШЕНИЯ:")
        print(f"Уравнение: {self.coef_A}x⁴ + {self.coef_B}x² + {self.coef_C} = 0")

        if not self.roots:
            print("Действительных корней нет")
        else:
            num_roots = len(self.roots)
            if num_roots == 1:
                print(f"Один корень: x = {self.roots[0]:.4f}")
            elif num_roots == 2:
                print(f"Два корня: x₁ = {self.roots[0]:.4f}, x₂ = {self.roots[1]:.4f}")
            elif num_roots == 3:
                print(f"Три корня: x₁ = {self.roots[0]:.4f}, x₂ = {self.roots[1]:.4f}, x₃ = {self.roots[2]:.4f}")
            elif num_roots == 4:
                print(f"Четыре корня: x₁ = {self.roots[0]:.4f}, x₂ = {self.roots[1]:.4f}, x₃ = {self.roots[2]:.4f}, x₄ = {self.roots[3]:.4f}")

            print("\nПроверка корней:")
            for root in self.roots:
                result = self.coef_A * (root**4) + self.coef_B * (root**2) + self.coef_C
                print(f"x = {root:8.4f} => {self.coef_A}·({root:.4f})⁴ + {self.coef_B}·({root:.4f})² + {self.coef_C} = {result:.6f}")


def main():
    print("ПРОГРАММА ДЛЯ РЕШЕНИЯ БИКВАДРАТНЫХ УРАВНЕНИЙ")
    print("Уравнение вида: Ax⁴ + Bx² + C = 0")

    equation = BiquadraticEquation()

    equation.get_coefficients()

    equation.solve()

    equation.print_solution()


if __name__ == "__main__":
    main()
