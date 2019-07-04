"""
page = Pagination(request.GET.get('page'), all_depart.count(), per_num=10, max_show=11  )

数据[page.start:page.end]

前端展示的HTML page.page_html

"""

from django.utils.safestring import mark_safe

class Pagination:
    
    def __init__(self, page_num, all_count, per_num=10, max_show=11):
        try:
            page_num = int(page_num)
        except Exception as e:
            page_num = 1
        
        self.page_num = page_num
        # 总数据量
        all_count = all_count
        # 每页显示的数据
        self.per_num = per_num
        
        # 最大显示页码数
        self.max_show = max_show
        self.half_show = max_show // 2
        
        # total_num 总页码数
        self.total_num, more = divmod(all_count, per_num)
        
        if more:
            self.total_num += 1
    @property
    def start(self):
        return (self.page_num - 1) * self.per_num

    @property
    def end(self):
        return self.page_num * self.per_num

    @property
    def page_html(self):
        # 能显示的页面数少于最大显示页码数
        if self.total_num < self.max_show:
            page_start = 1
            page_end = self.total_num
        else:
            # 左边极值
            if self.page_num <= self.half_show:
                page_start = 1
                page_end = self.max_show
            
            elif self.page_num + self.half_show > self.total_num:
                
                page_start = self.total_num - self.max_show + 1
                page_end = self.total_num
            else:
                # 页码的起始值
                page_start = self.page_num - self.half_show
                # 页码的终止值
                page_end = self.page_num + self.half_show
        
        page_list = []
        
        if self.page_num == 1:
            page_list.append(
                '<li class="disabled"><a  aria-label="Previous"><span aria-hidden="true">&laquo</span> </a></li>')
        else:
            page_list.append(
                '<li><a href="?page={}" aria-label="Previous"><span aria-hidden="true">&laquo</span> </a></li>'.format(
                    self.page_num - 1))
        
        for i in range(page_start, page_end + 1):
            
            if i == self.page_num:
                page_list.append('<li class="active"><a href="?page={}">{}</a></li>'.format(i, i))
            else:
                page_list.append('<li><a href="?page={}">{}</a></li>'.format(i, i))
        
        if self.page_num == self.total_num:
            page_list.append(
                '<li class="disabled"><a  aria-label="Previous"><span aria-hidden="true">&raquo;</span> </a></li>')
        else:
            page_list.append(
                '<li><a href="?page={}" aria-label="Previous"><span aria-hidden="true">&raquo;</span> </a></li>'.format(
                    self.page_num + 1))
        
        return mark_safe(''.join(page_list))
