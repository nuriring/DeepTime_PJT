from re import A
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .serializers.ott import OttSerializer
from .models import Movie, Ott,Review, Genre
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers.movie import MovieListSerializer,MovieSerializer
from .serializers.review import ReviewListSerializer, ReviewSerializer
from .serializers.ott import MovieOttSerializer
from rest_framework import status




# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.method =='GET':
        #like_count 개수 추가
        movies = Movie.objects.annotate(
            like_count=Count('like_users', distinct=True)
        ).order_by('-popularity')[0:100] #인기순으로 정렬 #장르순으로 정렬 시리얼라이저 추가로 만들고 무비리스트 한개더 만들어야 할듯?
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def genre_movie_list(request, genre_pk):
    if request.method =='GET':
        genre = Genre.objects.get(pk=genre_pk)
        movies = genre.movies.annotate(
            like_count=Count('like_users', distinct=True)
        ).order_by('-pk')[0:100]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
@api_view(['GET', 'POST']) #리뷰 리스트 조회를 따로 만들 필요가 있나?
def create_review(request, movie_pk):

    def review_list():
        reviews = Review.objects.order_by('-pk')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    def create_review():
        user = request.user
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)

            # 기존 serializer 가 return 되면, 단일 review 만 응답으로 받게됨.
            # 사용자가 댓글을 입력하는 사이에 업데이트된 review 확인 불가 => 업데이트된 전체 목록 return 
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return create_review()

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def review_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)

    if request.method == 'GET':
        return review_detail()
    elif request.method == 'PUT':
        if request.user == review.user:
            return update_review()
    elif request.method == 'DELETE':
        if request.user == review.user:
            return delete_review()


@api_view(['GET'])
def ott_list(request, provider_name):
    if request.method =='GET':
        # ott_movies = get_list_or_404(Ott, provider_name=provider_name)
        # serializer = OttSerializer(ott_movies, many=True)
        # print(type(serializer.data))
        ott_movies = get_list_or_404(Ott, provider_name=provider_name)
        movies_id = []
        movies = []
        serializer = OttSerializer(ott_movies, many=True)
        for i in range(len(serializer.data)):
            movies_id.append((list(serializer.data))[i]['movie_id'])
        for i in range(len(movies_id)):
            num = movies_id[i]
            print(num)
            movie = Movie.objects.get(pk=num)
            movie_serializer = MovieOttSerializer(movie)
            movies.append(movie_serializer.data)
        # print(movies)
        return Response(movies)
        # # print(len(serializer.data))
        # # print((list(serializer.data))[0]['movie_id'])
