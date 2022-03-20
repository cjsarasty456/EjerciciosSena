using BlazorCrud.Model;
using Dapper;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Threading.Tasks;

namespace BlazorCrud.Data.Dapper.Repositorios
{
    public class FilmRepository : IFilmRepository
    {
        private string ConnectionString;

        public FilmRepository(string connectionString)
        {
            ConnectionString = connectionString;
        }
        protected SqlConnection dbConnection()
        {
            return new SqlConnection(ConnectionString);
        }
        public Task<bool> DeleteFilm(int id)
        {
            throw new NotImplementedException();
        }

        public Task<IEnumerable<Film>> GetAllFilms()
        {
            throw new NotImplementedException();
        }

        public Task<Film> GetFilmDetails(int id)
        {
            throw new NotImplementedException();
        }

        public async Task<bool> InsertFilm(Film film)
        {
            var db = dbConnection();
            using (var connection = new SqlConnection(ConnectionString))
            {

            
                var sql = @"
                        insert into (Title, Director, ReleaseDate) 
                        values('"+film.Title+ "', '" + film.Director + "', '" + film.ReleaseDate + "')";
            var result = await connection.ExecuteAsync(sql); 
            return result>0;
            }
        }

        public Task<bool> UpdateFilm(Film film)
        {
            throw new NotImplementedException();
        }
    }
}
