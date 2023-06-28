class ViewSale:
    @staticmethod
    def render(*data) -> None:
        print('----> Vendas efetuadas <----',
            '\n'.join(data[1]), 
            f'Total registros: {data[0]}\n', sep="\n")