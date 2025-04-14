import pytest
from amount_banquet2 import Amount_page  # your_module.py に Amount_page クラスがあるとして

def test_amount_calculation_basic():
    root_mock = pytest.importorskip("tkinter").Tk()
    page = Amount_page(root_mock, "テストプラン", "スタンダード", 2, 1, "2025-04-11")
    page.day_select.set(2)
    page.big_people_entry.delete(0, "end")
    page.big_people_entry.insert(0, "2")
    page.small_people_entry.delete(0, "end")
    page.small_people_entry.insert(0, "1")
    page.amount_button()  # 金額表示ボタンの処理を実行
    assert page.sum_amount > 0  # 合計金額が計算されているか
    root_mock.destroy()

def test_amount_calculation_with_room_upgrade():
    root_mock = pytest.importorskip("tkinter").Tk()
    page = Amount_page(root_mock, "テストプラン", "岩手山展望露天風呂付き和室", 2, 0, "2025-04-11")
    page.day_select.set(1)
    page.big_people_entry.delete(0, "end")
    page.big_people_entry.insert(0, "2")
    page.amount_button()
    initial_amount = page.sum_amount
    page.option_window()
    # オプションで何か選択する操作 (例: 追加料理を1つ選択)
    if page.addmeal_combos:
        page.addmeal_combos[0][0].set("1")
    page.calculate_total()
    page.amount_button() # 再度金額表示
    assert page.sum_amount > initial_amount # オプション料金が加算されているか
    root_mock.destroy()