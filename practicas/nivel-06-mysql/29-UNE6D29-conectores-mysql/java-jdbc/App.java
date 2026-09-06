import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public final class App {
    private static String env(String name, String fallback) {
        String value = System.getenv(name);
        return value == null || value.isBlank() ? fallback : value;
    }

    public static void main(String[] args) throws Exception {
        String host = env("MYSQL_HOST", "127.0.0.1");
        String port = env("MYSQL_PORT", "3306");
        String user = env("MYSQL_USER", "root");
        String password = env("MYSQL_PASSWORD", "");
        String url = "jdbc:mysql://" + host + ":" + port
            + "/une6d29_connectors?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true";

        String sql = """
            SELECT contact_id, full_name, email, city, created_at
            FROM contacts
            ORDER BY contact_id
            """;

        try (
            Connection connection = DriverManager.getConnection(url, user, password);
            PreparedStatement statement = connection.prepareStatement(sql);
            ResultSet result = statement.executeQuery()
        ) {
            while (result.next()) {
                System.out.printf(
                    "%d | %s | %s | %s | %s%n",
                    result.getLong("contact_id"),
                    result.getString("full_name"),
                    result.getString("email"),
                    result.getString("city"),
                    result.getTimestamp("created_at")
                );
            }
        }
    }
}
