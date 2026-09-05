using MySql.Data.MySqlClient;

static string Env(string name, string fallback)
{
    string? value = Environment.GetEnvironmentVariable(name);
    return string.IsNullOrWhiteSpace(value) ? fallback : value;
}

string host = Env("MYSQL_HOST", "127.0.0.1");
string port = Env("MYSQL_PORT", "3306");
string user = Env("MYSQL_USER", "root");
string password = Env("MYSQL_PASSWORD", "");

string connectionString =
    $"Server={host};Port={port};Database=une6d29_connectors;User ID={user};Password={password};SslMode=Preferred;";

await using MySqlConnection connection = new(connectionString);
await connection.OpenAsync();

const string sql = """
    SELECT contact_id, full_name, email, city, created_at
    FROM contacts
    ORDER BY contact_id
    """;

await using MySqlCommand command = new(sql, connection);
await using MySqlDataReader reader = await command.ExecuteReaderAsync();

while (await reader.ReadAsync())
{
    Console.WriteLine(
        $"{reader.GetInt64("contact_id")} | " +
        $"{reader.GetString("full_name")} | " +
        $"{reader.GetString("email")} | " +
        $"{reader.GetString("city")} | " +
        $"{reader.GetDateTime("created_at"):O}"
    );
}
