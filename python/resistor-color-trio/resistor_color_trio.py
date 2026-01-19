def label(colors):
    color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

    value = (
        (color_list.index(colors[0]) * 10 +
         color_list.index(colors[1]))
        * (10 ** color_list.index(colors[2]))
    )

    if value < 1_000:
        return f"{value} ohms"
    elif value < 1_000_000:
        return f"{value // 1_000} kiloohms"
    elif value < 1_000_000_000:
        return f"{value // 1_000_000} megaohms"
    else:
        return f"{value // 1_000_000_000} gigaohms"