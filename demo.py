import thumbnail

if __name__ == '__main__':

    params = {
        'images': './data/input/images/',
        'sentences': './data/input/sentences/sentences.txt',
        'font': './data/input/fonts/theboldfont.ttf',
        'output': './data/output/',
    }

    thumbnail.generate(**params)
