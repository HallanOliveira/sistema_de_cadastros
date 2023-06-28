class ViewClient:
    @staticmethod
    def render(*data) -> None:
        print('----> Clientes cadastrados <----',
            '\n'.join(data[1]), 
            f'Total registros: {data[0]}\n', sep="\n")