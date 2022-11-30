if __name__ == '__main__':
    s = input()
    print("yes" if s.lower()[-3::] == '.py' else "no")
