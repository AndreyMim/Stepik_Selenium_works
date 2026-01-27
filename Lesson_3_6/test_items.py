from time import sleep



def test_user_should_see_basket(browser):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    sleep(5)
    basket_button = browser.find_elements('class name', 'btn-add-to-basket')
    assert basket_button, f'Button "Add to basket" not present'

if __name__ == "__main__":
    main()