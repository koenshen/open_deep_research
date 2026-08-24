# From Java Servlets to Spring Boot: A Comprehensive Evolution

## Introduction

The journey of Java web development from the mid-1990s to today is a story of progressive simplification. Each iteration—from Servlets and JSP, through EJB, Spring Framework, Spring MVC, to Spring Boot—was designed to solve specific pain points in the previous generation. This report traces that evolution, explains the core functionalities of the modern Spring ecosystem, and provides a practical guide for developers working with Spring Boot today.

---

## 1. Historical Evolution

### 1.1 Java Servlets and JSP (Mid‑1990s – Early 2000s)

**What problems were solved?**

Servlets were introduced to replace the Common Gateway Interface (CGI) for generating dynamic web content. CGI had severe limitations:

- **Performance**: Each request spawned a heavyweight OS process; Servlets use lightweight threads.
- **Scalability**: CGI could not scale because of per‑request process overhead.
- **Portability**: CGI was platform‑dependent; Servlets run on any JVM.
- **Session management**: CGI had no built‑in session tracking; Servlets provide `HttpSession`.
- **Security**: Servlets benefit from Java’s security model.

**Key features of Servlets**

A servlet is a Java class that extends `HttpServlet` and overrides `doGet()` / `doPost()`. It must be deployed with a descriptor (`web.xml`) that maps URL patterns to the servlet class.

```java
// HelloWorldServlet.java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class HelloWorldServlet extends HttpServlet {
    private int counter = 0;

    public void init() { /* initialization code */ }

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        counter++;
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<h1>Hello, World!</h1>");
        out.println("<p>Accessed " + counter + " times.</p>");
        out.println("</body></html>");
        out.close();
    }

    public void destroy() { /* cleanup */ }
}
```

**Pain points:**

- **Boilerplate code**: Parsing parameters, writing HTML, managing sessions manually.
- **Verbose XML configuration**: All servlet mappings lived in `web.xml`, which grew large.
- **Mixing presentation and logic**: JSP pages often contained Java scriptlets (`<% %>`), violating separation of concerns.
- **Manual request handling**: No framework support for validation, data binding, or error handling.

Sources: [1][2][3]

### 1.2 Enterprise JavaBeans (EJB) – The Heavyweight Era (1999–2005)

**What EJB aimed to solve**

EJB was Sun’s answer to enterprise concerns like declarative transactions, security, distributed computing, and persistence. It promised container‑managed services.

**Why EJB became notorious**

- **Complexity**: A simple entity bean required three Java files (home, remote/local, bean class) plus a massive deployment descriptor (`ejb-jar.xml`).
- **XML hell**: “For every line of business code you had to create at least 10 lines of framework code and two pages of XML.” [4]
- **Heavyweight programming model**: EJB forced developers to write container‑specific interfaces and follow strict lifecycle methods.
- **Testing difficulty**: Components could only be tested inside a full application server.
- **Vendor lock‑in**: EJB applications were tied to WebLogic, JBoss, or WebSphere.

**The downward spiral**

The EJB specification grew increasingly complex in an attempt to fix its own problems, leading to over‑engineering. By 2024, Jakarta EE 12 officially deprecated EJB, replacing it with CDI (Contexts and Dependency Injection) [5].

Sources: [4][5][6]

### 1.3 Spring Framework – The Lightweight Revolution (2002–2004)

**The birth of Spring**

Rod Johnson’s book *Expert One‑on‑One J2EE Design and Development* (2002) included 30,000 lines of supporting code (the `com.interface21` package). The core premise was that “J2EE often fails in practice not because of the technology itself, but because it is used badly” [7]. The sequel, *J2EE without EJB* (2004, with Juergen Hoeller), established a vision for lightweight, POJO‑based development.

**Key innovations**

- **Inversion of Control / Dependency Injection (IoC/DI)**: Instead of components looking up dependencies via JNDI, the container injects them into POJOs.
- **POJO‑centric**: Enterprise services (transactions, security) are applied to plain Java objects, not framework‑inherited classes.
- **Declarative programming via AOP**: Cross‑cutting concerns (logging, transactions) are handled through aspects, not through EJB container services.
- **XML‑based configuration (initially)**: Spring 1.0 used XML files to wire beans, but it was far simpler than EJB’s deployment descriptors.

```xml
<!-- applicationContext.xml – Spring 1.0 style -->
<bean id="productService" class="com.example.service.ProductService">
    <property name="productDao" ref="productDao"/>
</bean>
```

**Timeline**:

- **2003**: Spring 0.9 released under Apache 2.0 license.
- **March 2004**: Spring 1.0 GA.
- **2006**: Spring 2.0 with annotation support; surpassed 1M downloads.
- **2007**: Spring 2.5 introduced annotation‑based MVC controllers (`@MVC`).

Sources: [7][8][9]

### 1.4 Spring MVC – Annotations and REST (2007–2013)

**Problems Spring MVC solved compared to Struts**

Before Spring MVC, Apache Struts was the dominant MVC framework. Spring MVC offered:

- **Non‑invasive**: Controllers are POJOs, not forced to extend framework classes.
- **Annotation‑driven (`@RequestMapping`, `@RequestParam`, `@ModelAttribute`)**: Eliminated XML controller configuration.
- **Flexible method signatures**: Any number of request‑handling methods with flexible parameter types.
- **Better testing**: MockMvc and Spring TestContext provide excellent testability.
- **Multiple view technologies**: JSP, Thymeleaf, FreeMarker, etc.

**Key annotations (`@Controller`, `@RequestMapping`)**

```java
@Controller
@RequestMapping("/products")
public class ProductController {
    private final ProductService productService;

    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    @GetMapping
    public String listProducts(Model model) {
        model.addAttribute("products", productService.findAll());
        return "product/list";
    }
}
```

**@RestController (Spring 4.0, 2013)**

`@RestController = @Controller + @ResponseBody`. It returns data directly (JSON/XML) instead of views, making it ideal for REST APIs.

Sources: [10][11][12]

### 1.5 Spring Boot – The “Just Run” Manifesto (2014–Present)

**What problems did Spring Boot solve?**

Even with Spring MVC, developers still faced:

- **XML configuration complexity**: Traditional Spring required `web.xml`, `dispatcher-servlet.xml`, and other XML files.
- **Dependency version management**: Ensuring compatible versions of Spring modules and third‑party libraries was manual and error‑prone.
- **External application server setup**: Applications had to be deployed as WAR files to an installed Tomcat, Jetty, or JBoss.
- **Deployment friction**: “Works on my machine” issues were common due to differing server configurations.
- **Lack of opinionated defaults**: Developers had to make many decisions (which JSON library, which templating engine, how to configure the data source).

**Key innovations**

- **Auto‑configuration**: `@EnableAutoConfiguration` (included in `@SpringBootApplication`) scans the classpath and configures beans automatically based on dependencies and properties.
- **Starters**: Pre‑defined dependency descriptors (e.g., `spring-boot-starter-web`) that bundle compatible libraries with correct versions.
- **Embedded servers**: Applications run as standalone JARs with embedded Tomcat, Jetty, or Undertow.
- **Production‑ready features**: Actuator endpoints (`/actuator/health`, `/actuator/metrics`), health checks, metrics, and monitoring.
- **Externalized configuration**: `application.properties` / `application.yml` with profile‑specific overrides.

**Comparison: Servlet vs. Spring Boot Controller**

```java
// Old way: Servlet + web.xml
public class HelloServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        String name = request.getParameter("name");
        response.setContentType("application/json");
        PrintWriter out = response.getWriter();
        out.println("{\"message\": \"Hello, " + name + "!\"}");
        out.close();
    }
}
```

```java
// Spring Boot way
@RestController
@RequestMapping("/api")
public class HelloController {
    @GetMapping("/hello")
    public Greeting hello(@RequestParam(defaultValue = "World") String name) {
        return new Greeting("Hello, " + name + "!");
    }
    record Greeting(String message) {}
}
```

**Spring Boot Application class (all that’s needed to run):**

```java
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

**build.gradle** (one dependency for web):

```groovy
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
}
```

No XML, no external server setup. Just `java -jar application.jar`.

**Version history highlights**:

- **1.0** (April 2014) – First stable release by Pivotal.
- **2.0** (2018) – Spring 5, reactive support (WebFlux), Java 8+.
- **3.0** (2022) – Spring 6, Jakarta EE 9, Java 17 baseline, AOT & native‑image compilation.
- **4.0** (Nov 2025) – Spring 7, modularised auto‑configuration, Java 21+ baseline, OpenTelemetry starter.

Sources: [13][14][15][16]

---

## 2. Core Functionalities of the Spring Framework

### 2.1 Inversion of Control (IoC) / Dependency Injection (DI) Container

The `org.springframework.context.ApplicationContext` is the central interface for the IoC container. It manages the complete lifecycle of beans—from instantiation to destruction—and injects dependencies.

**BeanFactory vs. ApplicationContext**

| Feature | BeanFactory | ApplicationContext |
|---------|-------------|-------------------|
| Lazy initialization | Yes | Eager (singletons by default) |
| Annotations | No | Yes |
| Internationalization | No | Yes (MessageSource) |
| Event publishing | No | Yes |
| AOP | No | Yes (auto‑registration of BeanPostProcessors) |

**Dependency injection types**

- **Constructor injection** (recommended for mandatory dependencies): `public ProductService(ProductDao dao) { ... }`
- **Setter injection** (optional dependencies): `@Autowired public void setProductDao(ProductDao dao) { ... }`
- **Field injection** (discouraged): `@Autowired private ProductDao productDao;`

**Bean scopes**: Singleton (default), Prototype, Request, Session, Application.

**Stereotype annotations**:

- `@Component` – generic bean.
- `@Service` – service layer.
- `@Repository` – data access layer (adds persistence exception translation).
- `@Controller` / `@RestController` – web layer.

**Configuration methods**: XML (`<bean>`), Java (`@Configuration` + `@Bean`), and annotation (`@Component` + `@ComponentScan`).

Sources: [17][18][19]

### 2.2 Aspect‑Oriented Programming (AOP)

AOP separates cross‑cutting concerns (logging, security, transactions) from business logic.

**How Spring AOP works**: Spring uses **proxy‑based AOP** (JDK dynamic proxies or CGLIB) to wrap beans at runtime. Advice is applied only when a method is called through the proxy.

**Key concepts**:

- **Aspect**: A module of cross‑cutting concern (e.g., `@Aspect` class).
- **Join point**: Method execution (the only join point in Spring AOP).
- **Advice**: Action taken at a join point.
- **Pointcut**: Expression that selects join points (e.g., `execution(* com.example.service.*.*(..))`).
- **Target object**: Object being proxied.
- **Weaving**: Linking aspects to target objects (runtime only in Spring).

**Advice types**:

- `@Before` – runs before method execution.
- `@AfterReturning` – after successful return.
- `@AfterThrowing` – after exception.
- `@After (finally)` – after method regardless of outcome.
- `@Around` – most powerful; allows proceeding with the join point via `ProceedingJoinPoint`.

**Enabling AOP**: `@EnableAspectJAutoProxy`.

Sources: [20][21][22]

### 2.3 Spring MVC (Model‑View‑Controller)

**DispatcherServlet** is the front controller. It receives all incoming requests and delegates to handler mappings, adapters, and view resolvers.

**Request flow**:

1. Browser sends request.
2. `DispatcherServlet` receives it.
3. `HandlerMapping` finds the matching controller method (based on `@RequestMapping`).
4. `HandlerAdapter` invokes the method, populating arguments via `HandlerMethodArgumentResolvers`.
5. For `@Controller`: returns a view name → `ViewResolver` resolves to a template (e.g., Thymeleaf) → HTML.
6. For `@RestController`: returns data → `HttpMessageConverter` (e.g., Jackson) serializes to JSON.

**@Controller vs. @RestController**:

| Annotation | Returns | Default content type |
|------------|---------|----------------------|
| `@Controller` | View name (HTML) | `text/html` |
| `@RestController` | Data object (JSON/XML) | `application/json` |

**Key annotations**:

- `@RequestMapping` (and shortcuts: `@GetMapping`, `@PostMapping`, etc.)
- `@RequestParam`, `@PathVariable`, `@RequestBody`, `@ResponseStatus`
- `@ControllerAdvice` / `@RestControllerAdvice` for global exception handling.

Sources: [23][24][25]

### 2.4 Data Access / JDBC Abstraction / Transaction Management

**JdbcTemplate** eliminates boilerplate JDBC code (resource management, exception handling).

**Spring Data JPA** provides repository interfaces (e.g., `JpaRepository`) that automatically generate CRUD operations.

**Declarative transaction management** with `@Transactional`:

- The `PlatformTransactionManager` interface abstracts underlying transaction infrastructure (JDBC, JPA, JTA).
- `@Transactional` can be placed on classes or methods. It wraps the method in a transaction, committing on success and rolling back on runtime exceptions.

**Transaction propagation** (7 types):
- `REQUIRED` (default) – joins existing transaction or creates new one.
- `REQUIRES_NEW` – suspends existing and creates new.
- `NESTED` – uses savepoint within existing transaction.
- etc.

**Transaction isolation levels**:

| Level | Dirty read | Non‑repeatable read | Phantom read |
|-------|------------|---------------------|--------------|
| READ_UNCOMMITTED | Yes | Yes | Yes |
| READ_COMMITTED | No | Yes | Yes |
| REPEATABLE_READ | No | No | Yes |
| SERIALIZABLE | No | No | No |

**Rollback rules**: By default, only unchecked exceptions (`RuntimeException` and `Error`) trigger rollback. Checked exceptions do not. Use `rollbackFor` to customise.

**Common pitfalls**: Self‑invocation (calling a `@Transactional` method from within the same class bypasses the proxy) and calling `@Transactional` on private methods.

Sources: [26][27][28]

### 2.5 Spring Security

Spring Security is the de‑facto standard for authentication and access control in Spring applications.

**SecurityFilterChain**: A chain of servlet filters that intercept requests. Configuration is done by declaring a `SecurityFilterChain` bean (replacing the deprecated `WebSecurityConfigurerAdapter`).

**Authentication**: Uses `UserDetailsService` to load user data. Password encoding via `BCryptPasswordEncoder` (recommended).

**JWT support**:

- For stateless REST APIs, configure `SessionCreationPolicy.STATELESS`, disable CSRF, and add a JWT authentication filter.
- OAuth2 Resource Server with JWT: set `spring.security.oauth2.resourceserver.jwt.issuer-uri` and include `spring-security-oauth2-resource-server` and `spring-security-oauth2-jose`.

**Method‑level security**: `@EnableMethodSecurity` + `@PreAuthorize("hasRole('ADMIN')")` – fine‑grained SpEL expressions.

**CORS**: Must be configured at the Spring Security level (not just `@CrossOrigin`) because Spring Security processes requests before MVC.

**Common mistakes**: Permitting all actuator endpoints, storing JWTs in localStorage, using `.antMatchers()` instead of `.requestMatchers()`.

Sources: [29][30][31]

### 2.6 Spring Boot Auto‑Configuration

**Auto‑configuration** inspects the classpath, existing beans, and properties to configure sensible defaults. The key annotation is `@EnableAutoConfiguration` (included in `@SpringBootApplication`).

**How it works**:

1. Spring Boot scans the classpath for `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`.
2. Each auto‑configuration class uses conditional annotations:
   - `@ConditionalOnClass` – if a class is on the classpath.
   - `@ConditionalOnMissingBean` – if no user‑defined bean of that type exists.
   - `@ConditionalOnProperty` – if a property is set.
   - `@ConditionalOnWebApplication` – if the application is a web app.
3. Beans are registered dynamically. User‑defined beans always take priority.

**Starters** are pre‑built dependency descriptors. For example, `spring-boot-starter-web` includes Spring MVC, Jackson, embedded Tomcat, and HTTP converters.

**Debugging**: Set `debug=true` in `application.properties` to see positive/negative matches.

Sources: [32][33][34]

### 2.7 Embedded Servers and Production‑Ready Features (Actuator)

**Embedded servers**: By default Spring Boot embeds Tomcat (via `spring-boot-starter-web`). Alternatives: Jetty, Undertow. The application runs as a standalone JAR, eliminating the need for an external server.

**Spring Boot Actuator** exposes operational endpoints:

| Endpoint | Purpose |
|----------|---------|
| `/actuator/health` | Application health (UP/DOWN) |
| `/actuator/metrics` | JVM, CPU, HTTP metrics |
| `/actuator/info` | Custom application info |
| `/actuator/beans` | All Spring beans |
| `/actuator/env` | Environment properties |
| `/actuator/loggers` | Logger configuration |

**Micrometer** integration provides a vendor‑neutral facade for metrics collection (e.g., Prometheus, DataDog).

**Health indicators**: Built‑in checks for databases, disk space, Redis, RabbitMQ, etc. Custom HealthIndicator can be implemented.

**Security**: In production, restrict actuator endpoints with Spring Security, use a separate management port, or expose only `/health` and `/info`.

Sources: [35][36][37]

---

## 3. Essential Developer Knowledge

### 3.1 Core Annotations

**`@SpringBootApplication`** – combines `@Configuration`, `@EnableAutoConfiguration`, `@ComponentScan`. It is the entry point of any Spring Boot application.

**`@Controller`** – marks a class as a web controller (returns views). **`@RestController`** – combines `@Controller` and `@ResponseBody` (returns data directly).

**`@RequestMapping`** and its shortcut variants: `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`, `@PatchMapping`.

**Stereotype annotations**: `@Service`, `@Repository`, `@Component` – identify Spring‑managed beans. `@Repository` adds persistence exception translation.

**`@Autowired`** – injects dependencies. **Prefer constructor injection** over field injection for immutability and testability. Use `@Qualifier` to disambiguate.

**`@Configuration`** + **`@Bean`** – define beans in Java configuration classes.

**`@Value`** – injects property values. **`@ConfigurationProperties`** – binds structured configuration to type‑safe POJOs (preferred over `@Value` for related properties).

**`@Transactional`** – manages transaction boundaries. Must be on public methods; self‑invocation bypasses the proxy.

**`@ExceptionHandler`** – handles exceptions in a single controller. **`@ControllerAdvice`** / **`@RestControllerAdvice`** – global exception handling across all controllers.

**`@CrossOrigin`** – enables CORS at the controller level. For global CORS with Spring Security, use `http.cors()` and a `CorsConfigurationSource` bean.

**`@Valid`** or **`@Validated`** – triggers Bean Validation on request bodies.

Sources: [38][39][40]

### 3.2 Application Properties and YAML Configuration

Spring Boot externalises configuration via `application.properties` or `application.yml`. YAML is often preferred for its hierarchical structure.

**Example `application.yml`**:

```yaml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: user
    password: ${DB_PASSWORD}
  jpa:
    hibernate:
      ddl-auto: update
```

**Profile‑specific files**: `application-dev.yml`, `application-prod.yml` – activated via `spring.profiles.active`.

**Configuration precedence** (highest to lowest):

1. Command‑line arguments (`--server.port=9090`)
2. Environment variables
3. Profile‑specific files
4. `application.properties` / `application.yml` in the JAR

**Best practices**:

- Never commit secrets (passwords, API keys) to source control. Use environment variables or a vault.
- Use `@ConfigurationProperties` for groups of related properties.
- Validate configuration on startup using `@Validated`.

Sources: [41][42]

### 3.3 Dependency Management with Maven/Gradle and Starters

**Maven** – inherit from `spring-boot-starter-parent`:

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.5.0</version>
</parent>
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

**Gradle** – use the Spring Boot plugin:

```groovy
plugins {
    id 'org.springframework.boot' version '3.5.0'
    id 'io.spring.dependency-management' version '1.1.7'
}
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
}
```

**Spring Boot Starters** are grouped by functionality:

| Starter | Purpose |
|---------|---------|
| `spring-boot-starter-web` | Web (Spring MVC + embedded Tomcat) |
| `spring-boot-starter-data-jpa` | JPA + Hibernate |
| `spring-boot-starter-security` | Spring Security |
| `spring-boot-starter-test` | JUnit 5, Mockito, AssertJ, Testcontainers |
| `spring-boot-starter-actuator` | Production monitoring |

**Version management**: The BOM (`spring-boot-dependencies`) defines curated versions. Override only when necessary, and test thoroughly.

Sources: [43][44]

### 3.4 Building RESTful APIs

**Basic structure**:

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping
    public List<User> getAllUsers() { ... }

    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id) { ... }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public User createUser(@Valid @RequestBody User user) { ... }

    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @Valid @RequestBody User user) { ... }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteUser(@PathVariable Long id) { ... }
}
```

**Error handling** with `@RestControllerAdvice`:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(ResourceNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ErrorResponse handleNotFound(ResourceNotFoundException ex) {
        return new ErrorResponse(ex.getMessage());
    }
}
```

**Content negotiation**: The client can request JSON or XML via the `Accept` header. Spring Boot includes Jackson by default.

**HATEOAS**: Use `spring-boot-starter-hateoas` to add hypermedia links to responses.

Sources: [45][46]

### 3.5 Testing Strategies

**Unit testing** – test individual classes in isolation:

- Use `@ExtendWith(MockitoExtension.class)` + `@Mock` / `@InjectMocks`.
- Do **not** load the Spring context for pure unit tests.
- Follow the AAA pattern (Arrange, Act, Assert).

**Integration testing** – verify the full stack:

- `@SpringBootTest` loads the entire application context (use for ~20% of tests).
- `@WebMvcTest(MyController.class)` – loads only the web layer, ideal for controller tests with MockMvc.
- `@DataJpaTest` – loads only JPA components, uses an in‑memory database.

**MockMvc example**:

```java
@WebMvcTest(UserController.class)
class UserControllerTest {
    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Test
    void shouldReturnAllUsers() throws Exception {
        when(userService.findAll()).thenReturn(List.of(new User("Alice")));

        mockMvc.perform(get("/api/users")
                .accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].name").value("Alice"));
    }
}
```

**Database testing with Testcontainers**:

```java
@Testcontainers
@SpringBootTest
class UserRepositoryTest {
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Autowired
    private UserRepository userRepository;

    @Test
    void shouldSaveUser() {
        userRepository.save(new User("Bob"));
        assertThat(userRepository.findAll()).hasSize(1);
    }
}
```

Sources: [47][48][49]

### 3.6 Common Pitfalls and Best Practices

**Pitfalls**:

1. **Self‑invocation of `@Transactional` methods** – calling a `@Transactional` method from within the same class bypasses the proxy. **Fix**: move the transactional method to a separate bean.
2. **Circular dependencies** – Spring Boot 2.6+ prohibits circular references by default. **Fix**: use `@Lazy`, extract a shared service, or use setter injection.
3. **`LazyInitializationException`** – accessing lazy‑loaded JPA associations outside a transaction. **Fix**: use `JOIN FETCH` in queries or return DTOs.
4. **Exposing actuator endpoints in production** – the Volkswagen data leak was caused by an open `/actuator/heapdump`. **Fix**: expose only necessary endpoints and secure them with Spring Security.
5. **Using `@Value` for complex configuration** – prefer `@ConfigurationProperties` for type‑safe binding.
6. **Ignoring `@Transactional` on private methods** – Spring AOP only proxies public methods; the annotation is silently ignored.
7. **Not handling `AuthenticationException` / `AccessDeniedException` in REST APIs** – return structured JSON error responses instead of default HTML.

**Best practices**:

- **Use constructor injection** for mandatory dependencies (improves testability and immutability).
- **Follow the Controller → Service → Repository pattern** – keep controllers thin, services stateless, repositories focused on data access.
- **Validate input thoroughly** with `@Valid` and custom validators.
- **Use `@ConfigurationProperties` for configuration** – it’s cleaner and testable.
- **Enable DevTools only in development** – use `runtimeOnly 'org.springframework.boot:spring-boot-devtools'` in Gradle.
- **Profile early and often** – use Actuator, Micrometer, and Prometheus/Grafana.
- **Keep business logic out of controllers** – services should contain all business rules.
- **Use `@PreAuthorize` for method‑level security** – fine‑grained access control with SpEL.
- **Write tests in the 80/20 ratio** – 80% unit tests, 20% integration tests.
- **Understand the underlying Spring Framework** – Spring Boot is built on Spring; knowledge of IoC, AOP, and bean lifecycle is essential.

Sources: [50][51][52][53]

---

### Sources

[1] Java Servlets vs CGI comparison: https://www.slideshare.net/slideshow/java-servlets-and-cgi/113362281

[2] Servlets and JSP Overview: https://medium.com/@utkarsh.jain2199/-c3ec44223011

[3] Introduction to Java Servlets: https://www.geeksforgeeks.org/java/introduction-java-servlets

[4] Microservices Are Becoming the New EJB: https://levelup.gitconnected.com/we-escaped-ejb-hell-then-we-built-it-again-and-called-it-microservices-b3373747c18e

[5] Jakarta EE 12: The Death of Enterprise JavaBeans: https://medium.com/javarevisited/jakarta-ee-12-the-death-of-enterprise-javabeans-4132a0ab6a9d

[6] What’s Wrong With EJB: https://wiki.c2.com?WhatsWrongWithEjb=

[7] Expert One-on-One J2EE Design and Development: https://www.amazon.com/Expert-One-One-Design-Development/dp/0764543857

[8] Spring Framework History and Structure: https://dev.to/jeanv0/spring-framework-history-and-its-structure-361

[9] Spring Framework: The Origins of a Project and a Name: https://spring.io/blog/2006/11/09/spring-framework-the-origins-of-a-project-and-a-name

[10] Spring @RequestMapping Annotation with Example: https://www.geeksforgeeks.org/springboot/spring-requestmapping-annotation-with-example

[11] 10 Examples of @RequestMapping Annotation: https://javarevisited.blogspot.com/2024/04/10-examples-of-requestmapping.html

[12] Difference between @Controller vs @RestController: https://symflower.com/en/company/blog/2024/controller-restcontroller-spring-boot

[13] Spring Boot simplifies Spring development: https://www.linkedin.com/posts/bridgeflair-llc_spring-boot-is-a-framework-built-on-top-of-activity-7420646941534924800-fXKC

[14] Spring vs Spring Boot: Understanding Starters, Auto-Configuration: https://medium.com/@vishipatil/day-1-spring-vs-spring-boot-understanding-starters-auto-configuration-03f513ba0299

[15] Spring Boot History and Version History: https://learncodewithdurgesh.com/tutorials/spring-boot-tutorials/spring-boot-history-and-version-history

[16] Spring Boot 4 Modularization: https://www.danvega.dev/blog/spring-boot-4-modularization

[17] The IoC Container – Spring Framework Reference: https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/beans.html

[18] The Spring ApplicationContext: https://www.baeldung.com/spring-application-context

[19] BeanFactory vs ApplicationContext in Spring: https://www.geeksforgeeks.org/springboot/beanfactory-vs-applicationcontext-in-spring

[20] Aspect Oriented Programming with Spring: https://docs.spring.io/spring-framework/docs/2.5.5/reference/aop.html

[21] Spring AOP Tutorial: https://www.edureka.co/blog/spring-aop-tutorial

[22] Spring AOP Example Tutorial: https://www.digitalocean.com/community/tutorials/spring-aop-example-tutorial-aspect-advice-pointcut-joinpoint-annotations

[23] Spring MVC: https://medium.com/@yunussiddiqui55/spring-mvc-337d781473d9

[24] What is Spring MVC: @Controllers & @RestControllers: https://www.marcobehler.com/guides/spring-mvc

[25] Mapping Requests :: Spring Framework: https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-requestmapping.html

[26] Transaction Management – Spring Framework 4.1.x: https://docs.spring.io/spring-framework/docs/4.1.x/spring-framework-reference/html/transaction.html

[27] Transaction Propagation and Isolation in Spring @Transactional: https://www.baeldung.com/spring-transactional-propagation-isolation

[28] Spring Transaction Management: @Transactional In-Depth: https://www.marcobehler.com/guides/spring-transaction-management-transactional-in-depth

[29] OAuth 2.0 Resource Server JWT – Spring Security Reference: https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html

[30] Spring Boot Security Best Practices: Authentication, JWT, and OAuth2: https://katyella.com/blog/spring-boot-security-best-practices

[31] Implementing Spring Security 6 with Spring Boot 3: https://dev.to/pryhmez/implementing-spring-security-6-with-spring-boot-3-a-guide-to-oauth-and-jwt-with-nimbus-for-authentication-2lhf

[32] How Spring Boot Auto Configuration Works: https://www.youtube.com/watch?v=6u6PJXTb1cQ

[33] Spring Boot 3.x Auto-Configuration: https://paths.grasp.study/modules/93eabe43-d242-4aa1-9795-1648af66ec5c/lessons/4f2c6a0f-8c07-472b-b2d7-8d62e3f5d0a4

[34] How Spring Boot Auto-Configuration Works: https://medium.com/@AlexanderObregon/how-spring-boot-auto-configuration-works-68f631e03948

[35] Spring Boot Actuators: Expose Operational Info: https://dev.to/manojshr/spring-boot-actuators-to-expose-operational-info-2aok

[36] Monitoring Spring Boot Microservices with Actuator, Micrometer, and OpenTelemetry: https://uptrace.dev/blog/spring-boot-microservices-monitoring

[37] Spring Boot Actuator: Production-ready Features: https://docs.spring.io/spring-boot/reference/actuator/index.html

[38] 6 Main Spring Boot Annotations with Examples and Best Practices: https://www.jhkinfotech.com/blog/spring-boot-annotations-examples-and-best-practices

[39] Comprehensive Guide to Spring Annotations: https://medium.com/@sharmapraveen91/comprehensive-guide-to-spring-annotations-under-the-hood-working-43e9570002c4

[40] Using the @SpringBootApplication Annotation: https://docs.spring.io/spring-boot/reference/using/using-the-springbootapplication-annotation.html

[41] Externalized Configuration – Spring Boot Reference: https://docs.spring.io/spring-boot/reference/features/external-config.html

[42] Spring Boot Configuration Management Best Practices: https://blog.jetbrains.com/idea/2026/08/spring-boot-configuration-management-best-practices

[43] Build Systems :: Spring Boot: https://docs.spring.io/spring-boot/reference/using/build-systems.html

[44] Managing Dependencies – Spring Boot Gradle Plugin: https://docs.spring.io/spring-boot/gradle-plugin/managing-dependencies.html

[45] Building REST Services with Spring: https://spring.io/guides/tutorials/rest

[46] HATEOAS Links in Spring Boot REST APIs: https://medium.com/@AlexanderObregon/hateoas-links-in-spring-boot-rest-apis-2c33e3a9f03f

[47] Unit Testing in Spring Boot with JUnit and Mockito: https://www.djamware.com/post/unit-testing-in-spring-boot-with-junit-and-mockito

[48] Getting started with Testcontainers in a Java Spring Boot Project: https://testcontainers.com/guides/testing-spring-boot-rest-api-using-testcontainers

[49] Top 10 Spring Boot REST API Mistakes and How to Avoid Them: https://blog.devgenius.io/top-10-spring-boot-rest-api-mistakes-and-how-to-avoid-them-2025-update-1c73ef6e2c73

[50] Understanding the Self-Invocation Problem with @Transactional: https://medium.com/@ebenezerb/understanding-the-self-invocation-problem-with-transactional-annotation-in-spring-2b5b06286880

[51] Circular Dependencies in Spring: https://www.baeldung.com/circular-dependencies-in-spring

[52] Why `@Transactional` “Doesn’t Work” in Spring: 7 Proxy Gotchas: https://dev.to/thellu/why-transactional-doesnt-work-in-spring-7-proxy-gotchas-and-fixes-1l2b

[53] Securing Spring Boot Actuator Endpoints: https://paths.grasp.study/modules/7578db86-72da-483e-b8ac-8ce5999e4d5f/lessons/940546aa-5f07-49b7-91a5-88f4c1753b9a
