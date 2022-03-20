using BlazorCrud.Data.Dapper.Repositorios;
using BlazorCrud.Model;
using coreBlazorCRUD.UI.Data;
using coreBlazorCRUD.UI.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace coreBlazorCRUD.UI.Services
{
    public class FilmService : IFilmService
    {
        private readonly SqlConfiguration _configuration;
        private IFilmRepository _filmRepository;
        public FilmService(SqlConfiguration configuration)
        {
            _configuration = configuration;
            _filmRepository = new FilmRepository(configuration.ConnectionString);
        }
        public Task<bool> DeleteFilm(int id)
        {
            throw new NotImplementedException();
        }

        public Task<IEnumerable<Film>> GetAllFilms()
        {
            throw new NotImplementedException();
        }

        public Task<Film> GetDetails(int id)
        {
            throw new NotImplementedException();
        }

        public Task<bool> SaveFilm(Film film)
        {
            if (film.Id == 0)
                return _filmRepository.InsertFilm(film);
            else
                return null;
        }
    }
}