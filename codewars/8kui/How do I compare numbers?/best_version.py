def what_is(x):
    return {42: "everything", 42 * 42: 'everything squared'}.get(x, 'nothing')

print(what_is(42 * 42))