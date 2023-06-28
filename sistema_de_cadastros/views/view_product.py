class ViewProduct:
    @staticmethod
    def render(*data) -> None:
        print('----> Produtos cadastrados <----',
            '\n'.join(data[1]), 
            f'Total registros: {data[0]}\n', sep="\n")