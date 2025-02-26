
"""
- Onde começa?
No main tem uma chamada para um train_loader:
    train_dataset = DatasetFolder.ImageMaskFolder(
        train_dir,
        mask_dir,
        transforms.Compose([
            transforms.Resize(size=(img_size, img_size)),
            transforms.ToTensor(),
            normalize,
        ]))

E aí a gente indo até o train_dir, encontramos um caminho com augmented... então, a gente tem que entender como é que esse augmented foi feito.
Tem um arquivo chamado img_aug.py que pega um diretório de imagens train e um masks e cria um diretório train_augmented com imagens aumentadas.
Já que não tenho informações, vou construir a partir da base do kaggle.












"""
