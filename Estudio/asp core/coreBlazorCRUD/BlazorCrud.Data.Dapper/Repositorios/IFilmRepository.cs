using BlazorCrud.Model;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace BlazorCrud.Data.Dapper.Repositorios
{
    public interface IFilmRepository
    {
        Task<IEnumerable<Film>> GetAllFilms();
        Task<Film> GetFilmDetails(int id);
        Task<bool> InsertFilm(Film film);
        Task<bool> UpdateFilm(Film film);
        Task<bool> DeleteFilm(int id);
    }
}
