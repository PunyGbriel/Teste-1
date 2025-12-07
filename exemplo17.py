try:
    a = 5
    b = r
    r = a / b
except (ValueError, TypeError):
    print('Typer error')
except Exception as erro:
    print(f'error {erro.__class__}')
else:
    print(f'O resultado {r}')
finally:
    print('Volte sempre!!')