slist = []

print('Commands: \n'
      'check / c - Checks current List \n'
      'remove / r - Removes Items from the List'
      '[Anything else you type will be added to the List]')

while True:
    addlist = input('\n >>> ')
    slist.append(addlist)

    # - Check Function
    if addlist == 'check':
        slist.remove('check')
        for element in slist:
            print('- ', element)
    elif addlist == 'c':
        slist.remove('c')
        for element in slist:
            print('- ', element)
    # - Check Function

    # - Remove Function
    elif addlist == 'remove':
        slist.remove('remove')
        for element in slist:
            print('- ', element)
        Remove = input('Remove item and Item \n'
                       '>>> ')
        if Remove in slist:
            slist.remove(Remove)
        else:
            print('This Items does not seem to be in your list')
    elif addlist == 'r':
        slist.remove('r')
        for element in slist:
            print('- ', element)
        Remove = input('Remove item and Item \n'
                       '>>> ')
        if Remove in slist:
            slist.remove(Remove)
        else:
            print('This Items does not seem to be in your list')
    # - Remove Function
