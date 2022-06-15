from articles.models import Articles,ArticlesHits

def topArticles():
    articles = Articles.objects.all()
    data = [

    ]
    for ar in articles:
        articles_hits = ArticlesHits.objects.filter(article_id=ar.id).count()
        if articles_hits == 0:
            pass
        else:
            data.append({ar.id:articles_hits})

    result = []
    for r in sorted(data,key=max)[:5]:
        dict_to_tuple = r.popitem()
        result.append(dict_to_tuple[0])

    return result

def visitor_ip_address(request,article_id):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    check_article_hit = ArticlesHits.objects.filter(ip=ip,article_id=article_id).first()
    if check_article_hit is None:
        article_hit_create = ArticlesHits.objects.create(ip=ip,article_id=article_id)
 

    return ip