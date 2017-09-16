from miyadaiku.extend import jinja_global

@jinja_global
def get_prev_and_next_page(page, pagelist):
    pages = [page.load(p) for p in pagelist]
    for i, p in enumerate(pages):
        if p.is_same(page):
            index = i
            break
    else:
        return None, None

    prev = next = None
    if index:
        prev = pages[index-1]
    
    if index != (len(pages)-1):
        next = pages[index+1]

    return prev, next
