class ViewMenu:
    @staticmethod
    def render(options) -> None:
        print('---> Menu <---\n',
            '\n'.join(options), sep="\n")