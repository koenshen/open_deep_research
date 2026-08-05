# 从Java Servlets到Spring Boot：Java Web架构的演进与开发者必备知识

## 引言

Java Web技术的发展史是一部不断解决复杂性问题、提升开发效率的历史。从早期的CGI到如今的Spring Boot，每一次技术迭代都源于对前一代技术痛点的深刻反思。这篇报告将系统地追溯这段历史演进，深入剖析Spring Framework的核心功能，并为开发者提供从配置管理到安全实践的全方位知识指南。

---

## 第一部分：历史演进——从CGI到Spring Boot

### 1.1 CGI的局限性：Java Servlets之前的世界

在Java Servlets出现之前，动态Web内容生成的主要技术是**通用网关接口(Common Gateway Interface, CGI)**。CGI脚本通常使用Perl、C或Shell脚本编写，其工作模式是：每个HTTP请求创建一个新的操作系统进程来处理。

CGI的局限性极为严重：

- **性能开销巨大**：每个请求都创建一个新的操作系统进程，而Servlets使用每个请求一个线程（单个Servlet实例作为单例持久存在于JVM内存中，处理所有并发请求）。Servlets的创建成本比CGI低40-100倍，并且可以维护持久资源（如数据库连接池、缓存）[1]。

- **状态丢失**：CGI程序终止时所有状态丢失，下一个请求必须重新构建状态（通常从磁盘加载）。Servlets可在内存中保留重要状态并在请求间复用[1]。

- **可移植性差**：CGI脚本是原生操作系统可执行代码，而Servlets在JVM中运行，继承了Java的跨平台特性[1]。

- **安全隐患**：CGI脚本存在SQL注入等安全风险，在高流量场景下扩展性极差[1]。

### 1.2 Java Servlets（1990年代末）

Java Servlets作为运行在Servlet容器（如Tomcat、Jetty）中的服务器端Java组件，解决了CGI的核心问题。

**解决的问题**：

- **性能**：Servlets使用单个进程管理所有请求，消除了CGI的多进程开销，允许主进程在多个Servlet和请求间共享资源[1]。

- **可移植性**：继承了Java语言的跨平台特性，高效且可扩展[1]。

- **状态管理**：通过HttpSession对象、Cookie和URL重写支持会话管理和状态保持。HTTP本质上是一个无状态协议，Servlets为开发者提供了管理会话的工具[1]。

- **基于线程的并发**：每个新请求生成一个新线程而非新进程。Servlet容器在单个Servlet实例上通过线程管理多个请求[1]。

**Servlet请求/响应模型**：工作流程包括六个步骤：客户端发送请求→Web服务器接收→传递给Servlet→Servlet处理并生成响应→返回给服务器→服务器发送给客户端。Servlet容器创建HttpServletRequest和HttpServletResponse对象，为每个请求分配一个线程，调用service()方法，然后生成HTTP响应[1]。

**Servlet生命周期**：
1. **实例化**：构造函数调用一次（应用启动时或首次访问时）
2. **init()**：在生命周期中只调用一次，用于初始化
3. **service()**：每个请求调用一次，多线程执行，根据HTTP方法分发到doGet()/doPost()
4. **destroy()**：应用卸载或容器关闭时调用一次

**核心API层级**：`Servlet`接口 → `GenericServlet`（抽象类）→ `HttpServlet`（抽象类）→ 自定义类。开发者重写`doGet()`/`doPost()`方法[1]。

**Servlets的局限性**：
- 线程安全责任落在开发者身上
- 通过println语句生成HTML难以维护
- 阻塞线程模型浪费资源
- 参数绑定需要严格的允许列表机制

### 1.3 JavaServer Pages (JSP)（1999年）

Servlets虽然解决了CGI的问题，但引入了新问题：**将展示逻辑与业务逻辑混合在一起**。开发者被迫使用println()语句在Java代码中生成HTML，导致代码难以维护、阅读和修改。

JSP于1999年由Sun Microsystems发布，是一种基于Java的模板技术，用于动态生成Web页面。JSP文件（.jsp、.jspx、.jspf）在运行时被编译成Servlet。

**解决的问题**：

- **模板化动态内容生成**：JSP将Java代码嵌入HTML中使用`<% ... %>`标签，支持脚本片段、表达式和指令[2]。

- **关注点分离**：JSP适合开发视图内容，使用展示层帮助应用与用户交互。Model 2架构整合了Servlet和JSP：JSP用于展示层，Servlet用于处理任务，Servlet作为控制器处理请求并创建JSP页面所需的JavaBean[2]。

- **标签库**：JSP支持标准标签（useBean、getProperty、setProperty）、表达式语言(EL)和JSTL标签库（提供迭代和条件判断）[2]。

- **MVC架构支持**：JSP通常作为MVC架构中的视图组件，Servlet作为控制器。Apache Struts是第一个形式化的MVC框架[2]。

**JSP的批评**：Jason Hunter在2000年的文章《The Problems with JSP》中指出，JSP虽然将HTML从Servlet代码中移出，但仍然鼓励在页面中嵌入Java代码，使简单操作变得复杂，产生晦涩的错误信息，浪费磁盘和内存空间[2]。更好的实践是将JSP中的后端逻辑迁移到Servlet的Java代码中，保持清晰的分层。

### 1.4 Enterprise JavaBeans (EJB)（1999-2000年代）

EJB是Jakarta EE规范，用于服务器端企业级开发，通过应用服务器容器处理并发、安全、持久化和事务。EJB于1999年首次发布[3]。

**EJB试图解决的问题**：
- 分布式计算：提供标准化的分布式应用架构，支持集群、故障转移、有状态会话Bean、JMS、CORBA和分布式事务管理[3]
- 声明式事务：无需手动编写事务处理代码
- 安全：基于角色的声明式访问控制
- 可扩展性：通过对象池、钝化和激活管理大量并发用户

**EJB创造的严重问题**：

1. **极端复杂性**：EJB最大的问题是“设计委员会”式的复杂性，尤其是在事务方面提供了过多的模型和类型。在2000年代初期，Java开发被EJB和J2EE的复杂性所困扰，需要大量样板代码、XML配置和重量级容器[3]。

2. **重量级容器**：需要WebSphere、WebLogic、JBoss等复杂应用服务器，与容器API紧密耦合，XML配置复杂[3]。

3. **XML重型配置**：EJB 2.x要求至少三个Java类（远程/本地接口、Bean类）和强制性的部署描述符。部署描述符（META-INF/ejb-jar.xml）是强制性的，容器只有在提供部署描述符后才能识别EJB代码。EJB 2.X强制开发者实现甚至空实现的容器回调方法，如ejbCreate()、ejbPassivate()、ejbActivate()、ejbRemove()、setXXXContext()等[3]。

4. **可测试性差**：无法在EJB容器外部测试EJB模块，需要多个接口加上不必要的方法实现[3]。

5. **供应商锁定**：尽管声称可移植，但不同应用服务器的实现差异导致供应商锁定。

6. **冗长的异常处理**：EJB使用CORBA/RMI风格，强制代码捕获和处理大量异常（如RemoteException），导致代码混乱[3]。

**EJB 2.x vs EJB 3.x改进**：

EJB 3.0（2006年）引入了基于POJO的注解开发、可选的部署描述符、消除了强制接口和本地接口、添加了依赖注入、自定义拦截器、JPA 1.0、定时器服务，并将实体Bean替换为简单的POJO。EJB 3.1进一步增加了无接口视图、单例Bean、异步会话Bean、EJB Lite、允许EJB在.war文件内打包、标准化的全局JNDI访问和嵌入式容器测试支持[3]。

然而，EJB 2.x的坏名声很难清除。一位开发者回忆道：“我清楚地记得意识到EJB结束的那一刻。那是一个早晨，我盯着一个比大多数小说还长的部署描述符XML文件，试图向一个新工程师解释为什么我们需要十七个配置文件来将一条数据从一个服务移动到另一个服务。”[3]

### 1.5 Spring Framework（2002-2004年）

Spring Framework由**Rod Johnson**创建，随着他在2002年10月出版的《Expert One-on-One J2EE Design and Development》一书首次发布。该书包含了30,000行代码，包名为‘interface21’[4]。

该书的核心理念是“问题驱动，而非技术驱动”。Rod Johnson认为：“我提倡问题驱动而非技术驱动的方法（Sun的‘J2EE蓝图’可能弊大于利，因为它暗示了J2EE技术驱动的方法）。”[4]

书籍发布后，读者**Juergen Hoeller**和**Yann Caroff**通过Wrox论坛联系，请求将代码作为开源发布。Yann创造了‘Spring’这个名字，灵感来源于自然（Johnson曾在2000年徒步珠峰大本营）以及Spring代表传统J2EE“寒冬”后的新开始[4]。

Spring 0.9于2003年6月以Apache 2.0许可证发布，第一个里程碑版本1.0于2004年3月24日发布[4]。

**Spring如何解决EJB复杂性危机**：

1. **轻量级容器**：Spring是一个轻量级容器，通常被视为EJB的替代品。Spring结合其丰富的支持功能，比通过EJB容器和EJB实现等效功能更好的选择[4]。

2. **POJO开发**：Spring致力于使开发者能够使用POJO构建应用。核心优势在于放弃平台特定和非标准化的组件，使Spring高度可移植且独立于应用服务器[4]。

3. **依赖注入**：DI是一种IoC形式，消除了对容器API的显式依赖；使用普通Java方法将依赖（如协作者对象或配置值）注入到应用对象实例中。Spring的IoC容器通过XML或Java注解管理Bean，支持构造函数注入、Setter注入和字段注入[4]。

4. **控制反转**：Spring的核心是一个IoC容器，通过依赖注入管理业务对象，消除了重型单例和复杂JNDI查找的需要[4]。

5. **无需应用服务器**：Spring可以在标准服务器（如Tomcat）上运行，无需完整的J2EE应用服务器。Spring支持向下扩展和向上扩展，在不同应用服务器之间可移植[4]。

6. **分层架构**：Spring提供分层架构，支持增量采用和轻松测试。Spring Framework（2003年）引入的IoC和DI实现了清晰的层次架构（Controller → Service → Repository）[4]。

7. **可测试性**：Spring从设计上就帮助开发者编写易于测试的代码。可测试性是一项特性——如果难以测试，就不会去测试[4]。

**Spring Framework主要模块**：
- **Spring Core Container**：IoC与依赖注入和自动装配
- **面向切面编程**：基于代理的切面织入，处理横切关注点
- **数据访问框架**：支持JDBC、ORM工具（如Hibernate和JPA）、NoSQL
- **事务管理**：通过PlatformTransactionManager支持本地和全局事务
- **模型-视图-控制器**：使用DispatcherServlet前端控制器模式的Web框架
- **远程访问框架**：RMI、SOAP、HTTP
- **Spring Boot**：约定优于配置的快速开发
- **Spring WebFlux**：响应式编程

**Spring Framework的主要版本**：
- Spring 1.0：2004年3月24日
- Spring 2.0：2006年10月
- Spring 2.5：2007年11月
- Spring 3.0：2009年12月
- Spring 4.0：2013年
- Spring 5.0：2017年9月28日
- Spring 6.0：2022年11月16日
- Spring 7.0：2025年

**关键里程碑**：2006年底达到100万次下载；2007年5月Interface21获得Benchmark的1000万美元A轮融资；2007年公司更名为SpringSource；2008年收购Covalent（Tomcat）和g2One（Groovy/Grails）；2009年8月VMware以4.2亿美元收购SpringSource[4]。

**传统Spring的局限性**：
虽然Spring解决了EJB复杂性危机，但引入了新问题：
- 仍然需要大量XML或Java配置
- 手动依赖版本管理
- 需要外部应用服务器部署
- 设置耗时长
- 手动WAR部署
- 学习曲线陡峭

### 1.6 Spring Boot（2014年）

到2010年代初期，虽然Spring相比EJB简化了企业Java开发，但开发者面临新的挑战：复杂配置、依赖管理负担、样板代码设置和外部服务器部署。

**Spring Boot的诞生**：核心洞察是：“如果我们保留Spring的强大功能但消除大部分配置会怎样？”[5]

Spring Boot 1.0.0于**2014年4月1日**由Pivotal发布为通用可用版本。Spring开发者倡导者Josh Long的口号是：“Make JAR, not WAR”[5]。

**Spring Boot核心特性**：

1. **自动配置**：Spring Boot基于类路径上的依赖和其他应用特定设置自动配置Spring应用。自动配置扫描依赖并使用@ConditionalOnClass等条件注解自动配置Bean。@SpringBootApplication包装了@EnableAutoConfiguration和@ComponentScan注解[5]。

2. **起步依赖**：Spring Boot提供有主见的“起步”依赖来简化构建配置。起步依赖是经过策划的依赖捆绑包，消除了版本冲突和依赖地狱。例如，spring-boot-starter-web包含Spring MVC、Tomcat、Jackson以及所有兼容版本的必需依赖。spring-boot-dependencies父POM定义了所有库版本，用户很少需要指定它们[5]。

3. **嵌入式服务器**：Spring Boot直接嵌入Tomcat、Jetty或Undertow（无需部署WAR文件），支持创建可直接使用`java -jar`运行的独立Spring应用。默认嵌入式服务器是Tomcat[5]。

4. **生产就绪功能**：Spring Boot提供度量、健康检查和外部化配置等生产就绪功能。Spring Boot Actuator通过HTTP端点或JMX暴露操作信息，包括健康状态、指标、环境配置、线程转储和Bean信息[5]。

5. **无需XML配置**：绝对不需要代码生成和XML配置要求[5]。

6. **Spring Initializr**：开发者可以通过start.spring.io引导项目，创建第一个应用无需XML或单独服务器设置[5]。

**Spring Boot如何支持微服务**：
- 独立可执行文件：每个微服务可以独立部署为单独进程
- 轻量级部署：速度、简洁性、现代微服务支持、生产就绪功能（监控、健康检查）和大型社区支持
- Spring Cloud（2015年）解决了分布式系统的服务发现、分布式配置、弹性模式和API网关问题
- 12-Factor应用原则：Spring Boot支持云原生应用的设计原则
- 约定优于配置：这是推动Spring Boot前进的关键一招

**Spring Boot的批评与局限性**：
- 自动配置作为黑盒：“自动配置是一个你不可能理解更不用说替换的黑盒”[5]
- 意外依赖：太多意外依赖问题
- 升级挑战：大规模迁移到3.x的复杂性
- Spring Boot 4的模块化：spring-boot-autoconfigure单一jar从1.0的182KB增长到3.5的2MB以上，在4.0中被拆分为按技术划分的模块，需要更明确的依赖管理

### 1.7 完整历史演进总结表

| 技术 | 时间 | 解决的问题 | 引入的新问题 | 被谁解决 |
|------|------|------------|-------------|---------|
| CGI | 1990年代初 | 动态Web内容 | 请求进程开销、可扩展性差、无状态管理、安全问题、不可移植 | Java Servlets |
| Java Servlets | 1990年代末（Servlet 2.1: 1999年1月） | CGI的多进程开销、线程并发、可移植性、状态管理、Java安全模型 | 通过println()生成HTML繁琐、展示与业务逻辑混合 | JSP |
| JSP | 1999年（JSP 1.0: 1999年6月） | 模板化动态内容、MVC关注点分离、标签库、表达式语言 | 仍然鼓励在页面中嵌入Java、简单操作复杂、错误信息晦涩、需要编译器 | MVC框架（Struts），然后是Spring MVC |
| EJB | 1999-2000年代 | 分布式计算、声明式事务、安全、可扩展性、标准化企业架构 | 极端复杂性、重量级容器、XML重型配置、可测试性差、供应商锁定、异常处理冗长 | Spring Framework |
| Spring Framework | 2002-2004年（1.0: 2004年3月） | EJB复杂性危机：轻量级POJO开发、IoC/DI、AOP、可测试性、无需应用服务器 | 大量XML/Java配置、手动依赖管理、外部服务器部署、学习曲线陡峭 | Spring Boot |
| Spring Boot | 2014年（1.0.0: 2014年4月） | 自动配置、起步依赖、嵌入式服务器、生产就绪功能、微服务支持、"约定优于配置" | 自动配置作为黑盒、意外依赖、大规模升级挑战、模块化复杂性 | 持续演进（Spring Boot 4模块化、Spring Native、GraalVM） |

---

## 第二部分：Spring Framework核心功能详解

### 2.1 依赖注入（DI）与控制反转（IoC）

**IoC与DI的概念**：**控制反转**是一种软件工程原则，将对象或程序部分的控制权转移给容器或框架。Spring Framework是最早使用IoC容器实现依赖注入的Java框架之一[6]。

传统上，对象负责创建和管理自己的依赖。IoC翻转了这个责任，将对象创建和依赖管理的控制权交给Spring框架。**依赖注入**是实现IoC的模式，被反转的控制是设置对象的依赖。DI有助于将松散耦合的类粘合在一起，同时保持它们的独立性[6]。

**IoC/DI的收益**：执行与实现解耦、轻松切换实现、更高的模块化、更易测试、高可维护性[6]。

**三种注入类型**：

- **构造函数注入**：通过构造函数参数提供依赖。推荐用于**必需依赖**，因为它确保对象在创建时完全初始化所有必需依赖，并支持不可变性[6]。

- **Setter注入**：对象构造后通过Setter方法提供依赖。推荐用于**可选依赖**[6]。

- **字段注入**：使用@Autowired直接注入字段。**不推荐**，因为反射开销、违反单一职责原则和可测试性挑战[6]。

**Bean生命周期与作用域**：

**Bean作用域**：
- **Singleton**（默认）：每个Spring IoC容器只创建一个Bean实例，所有对该Bean的请求返回同一个共享实例[6]
- **Prototype**：每次请求Bean时创建一个新实例
- **Request**：每个HTTP请求一个实例（仅在Web感知的ApplicationContext中有效）
- **Session**：每个HTTP会话一个实例
- **Application**：每个ServletContext一个实例

**Bean生命周期**：应用生命周期涉及处理环境变量、创建ApplicationContext、加载Bean定义、处理BeanFactoryPostProcessors和解析依赖。Singleton Bean默认预实例化，以尽早捕获配置问题。懒加载（lazy-init=true）将Bean创建延迟到首次请求，以更快的启动换取延迟的错误检测[6]。

**IoC容器：ApplicationContext与BeanFactory**：

- **BeanFactory**：IoC容器的基础接口，提供基本的IoC功能，包括依赖注入，使用**懒加载**初始化[6]。
- **ApplicationContext**：BeanFactory的完整超集，是Spring IoC容器的主要实现。提供额外功能包括事件处理、国际化、注解支持、AOP支持和默认**饿汉式**初始化[6]。

三种常见实现：`AnnotationConfigApplicationContext`、`ClassPathXmlApplicationContext`、`FileSystemXmlApplicationContext`。配置元数据可以通过XML、Java注解或Java代码提供[6]。

**自动装配模式与限定符**：

**自动装配模式**：`no`（无自动装配）、`byName`（按属性名）、`byType`（按属性类型，如果存在多个同类型Bean则抛出异常）、`constructor`（类似于byType但适用于构造函数参数）[6]。

**解决歧义**：当存在多个同类型Bean时，抛出`NoUniqueBeanDefinitionException`。解决方法：使用`@Primary`标记为主候选、使用`@Qualifier`指定精确的Bean名称、或使用显式Bean名称[6]。

### 2.2 面向切面编程（AOP）

**横切关注点**：AOP是一种编程范式，补充了面向对象编程。OOP的模块化单元是类，而AOP的模块化单元是切面。AOP解决了**横切关注点**的问题——跨越多个模块的功能，如日志、安全、错误处理和性能监控[7]。

**关键AOP概念**：

- **切面**：实现跨越多个类的横切关注点的类，如事务管理[7]
- **连接点**：应用执行流程中的特定点。在Spring AOP中，连接点**总是方法执行**[7]
- **切入点**：匹配连接点的谓词或表达式，决定是否执行通知[7]
- **通知**：在特定连接点执行的动作，即当匹配的连接点到达时被执行的切面方法[7]
- **目标对象**：被一个或多个切面通知的对象
- **AOP代理**：应用通知后创建的对象。如果目标实现接口则使用JDK动态代理，否则使用CGLIB代理[7]
- **织入**：将切面与应用对象链接的过程。Spring AOP在**运行时**使用基于代理的机制执行织入[7]

**五种通知类型**：
1. **@Before**：在连接点方法执行前执行
2. **@After**（finally）：连接点完成后执行，无论正常返回还是抛出异常
3. **@AfterReturning**：仅在连接点方法成功返回后执行
4. **@AfterThrowing**：仅在连接点方法抛出异常时执行
5. **@Around**：最强大的通知，包围连接点方法，可以选择是否执行连接点方法，使用ProceedingJoinPoint控制执行

**Spring AOP vs AspectJ**：
- Spring AOP使用**基于代理的运行时织入**（接口使用JDK动态代理，具体类使用CGLIB）
- AspectJ支持编译时、加载时和运行时织入
- Spring AOP仅支持Spring Bean上的方法执行连接点
- Spring AOP与IoC容器集成

**常见用例**：日志记录、事务管理、安全检查、性能监控、异常处理、缓存、审计日志[7]。

### 2.3 Spring MVC

**DispatcherServlet与请求处理管道**：Spring MVC围绕**前端控制器模式**设计，其中中央Servlet（DispatcherServlet）提供请求处理的共享算法，实际工作由可配置的委托组件执行。所有请求都通过DispatcherServlet[8]。

**HTTP请求处理流程**：
1. 客户端发送HTTP请求到特定URL
2. Web容器（如Tomcat）将请求路由到DispatcherServlet
3. DispatcherServlet询问**HandlerMapping**哪个控制器处理请求
4. HandlerMapping返回控制器详细信息（使用@RequestMapping注解标识适当的@Controller类）
5. DispatcherServlet将请求转发给相应的控制器
6. **控制器**处理请求，返回逻辑视图名称和模型给DispatcherServlet
7. DispatcherServlet咨询**ViewResolvers**确定实际视图（如JSP、Thymeleaf、Freemarker）
8. ViewResolver返回视图和扩展名
9. DispatcherServlet将模型和视图交给视图引擎
10. 视图引擎合并模板和模型数据以生成输出（HTML）
11. 渲染后的输出作为响应返回给客户端

DispatcherServlet非常可扩展，允许插入不同的适配器来执行许多任务。有超过30种不同的参数解析器实现，可以从请求中提取任何类型的信息并将其作为方法参数提供[8]。

**RESTful Web服务**：Spring提供`@RestController`（结合了@Controller和@ResponseBody），使用`HttpMessageConverter`（如MappingJackson2HttpMessageConverter）编组JSON。REST控制器方法使用`@RequestBody`和`@ResponseBody`直接从HTTP请求/响应体中读写，而不是返回视图名称[8]。

**内容协商**：允许客户端指定服务器响应格式的机制。单个端点可以以多种格式（如JSON和XML）提供结果。三种策略：URL后缀（如/user/2.json）、URL参数（如?format=xml）、Accept头策略（客户端设置Accept: application/xml或application/json）。Spring Boot默认仅支持JSON，要启用XML需添加jackson-dataformat-xml依赖[8]。

**异常处理**：Spring提供多种REST API异常处理方法：
- **@ExceptionHandler**：在控制器内本地使用或通过@ControllerAdvice/@RestControllerAdvice全局使用，支持返回ResponseEntity、ProblemDetail（RFC-9457）或使用@ResponseStatus
- **@ControllerAdvice**：生产应用推荐的最佳实践，集中处理全局异常，促进代码复用并保持控制器简洁
- **ResponseStatusException**（Spring 5）：控制器可以直接抛出ResponseStatusException，提供状态、原因和原因异常，适合原型开发但缺乏统一全局处理
- **@ResponseStatus on自定义异常**：简单但不适合REST API，因为它使用Servlet容器的HTML错误页面

### 2.4 数据访问

**JDBC抽象与JdbcTemplate**：Spring通过`JdbcTemplate`类提供JDBC抽象，内部基于Java SDK的JDBC API。JdbcTemplate通过处理资源管理和异常处理简化了JDBC——开发者只需专注于手头的任务。使用`?`作为参数以防止SQL注入攻击[9]。

关键特性：直接SQL执行完全控制、通过RowMapper（如BeanPropertyRowMapper）手动映射、参数化查询防止SQL注入、对需要精细控制的使用场景性能更佳[9]。

**ORM集成（Hibernate、JPA）**：Spring与ORM技术（包括Hibernate、JPA、Oracle Toplink和iBatis）集成，帮助简化数据库操作并减少SQL查询中的错误[9]。

**Spring Data JPA**：高级ORM抽象，具有最少的样板代码。使用@Entity、@Table、@Id注解的实体，扩展JpaRepository的仓库接口自动生成CRUD SQL查询，遵循命名约定的自定义查询方法（如findByAuthor），以及通过Pageable和Sort接口的分页和排序支持[9]。

**Spring Data JDBC**：比Spring Data JPA更简单的持久化框架，不提供缓存、懒加载、写后模式或模式生成。访问数据库时性能更好，但依赖数据库供应商[9]。

**Spring Data JPA vs JdbcTemplate**：Spring Data JPA适合需要利用ORM能力并直接使用领域模型的项目，JdbcTemplate适合需要对SQL查询进行精细控制的项目。两种方法可以在同一应用中共存[9]。

### 2.5 事务管理

**声明式 vs 程序式事务**：

- **声明式事务管理**：对应用代码影响最小，使用AOP将事务逻辑应用于方法，通过@Transactional注解或XML配置实现。优点：在任何环境中工作（不仅限于JTA）、适用于任何类、支持声明式回滚规则、允许自定义AOP通知[10]。

- **程序式事务管理**：使用TransactionTemplate进行显式事务控制，提供对事务边界的精细控制[10]。

**@Transactional注解及其属性**：

| 属性 | 描述 |
|------|------|
| **propagation** | 定义多个事务方法调用时事务之间的关系 |
| **isolation** | 定义一个事务中的操作与其他并发事务的隔离程度 |
| **timeout / timeoutString** | 事务在被强制回滚前应运行的最长时间（秒） |
| **readOnly** | 指示事务为只读，可通过允许数据库优化读操作来提升性能和并发性 |
| **rollbackFor / rollbackForClassName** | 特定异常类型的自定义回滚规则 |
| **noRollbackFor / noRollbackForClassName** | 不应触发回滚的异常 |
| **transactionManager** | 指定使用哪个PlatformTransactionManager（适用于多个事务管理器） |

**传播行为**：

| 传播类型 | 行为 |
|---------|------|
| **REQUIRED**（默认） | 加入现有事务或创建新事务 |
| **REQUIRES_NEW** | 挂起当前事务，创建新的独立事务 |
| **SUPPORTS** | 使用现有事务或以非事务方式执行 |
| **NOT_SUPPORTED** | 挂起任何当前事务，以非事务方式执行 |
| **MANDATORY** | 要求存在现有事务，不存在则抛出异常 |
| **NEVER** | 如果存在事务则抛出异常 |
| **NESTED** | 在现有事务内标记保存点（需要DataSourceTransactionManager或带JDBC支持的JPA） |

**隔离级别**：

| 隔离级别 | 脏读 | 不可重复读 | 幻读 |
|---------|------|-----------|------|
| **READ_UNCOMMITTED** | 允许 | 允许 | 允许 |
| **READ_COMMITTED** | 阻止 | 允许 | 允许 |
| **REPEATABLE_READ** | 阻止 | 阻止 | 允许 |
| **SERIALIZABLE** | 阻止 | 阻止 | 阻止 |

**默认@Transactional设置**：传播REQUIRED、隔离DEFAULT、读写、超时-1（无超时）、对RuntimeException/Error回滚但不包括已检查异常[10]。

**重要注意事项**：最常见的@Transactional陷阱是同一类中的自调用，绕过代理，导致REQUIRES_NEW等传播设置被忽略。Spring默认只支持公共方法上的@Transactional[10]。

**物理事务 vs 逻辑事务**：
- **物理事务**：实际的JDBC数据库事务
- **逻辑事务**：（可能嵌套的）@Transactional注解的Spring方法

对于PROPAGATION_REQUIRED，每个方法创建一个映射到同一物理事务的逻辑事务范围；内部回滚标记在外部提交时触发UnexpectedRollbackException。PROPAGATION_REQUIRES_NEW为每个范围使用独立的物理事务，不参与外部事务。PROPAGATION_NESTED使用带有JDBC保存点的单个物理事务，允许部分回滚而不影响外部事务[10]。

### 2.6 其他核心功能

**Spring表达式语言（SpEL）**：一种强大的表达式语言，支持在运行时查询和操作对象图。SpEL使用`#{ expression }`语法定义Bean定义，属性占位符使用`${...}`[11]。核心功能包括字面表达式、布尔和关系运算符、正则表达式、类表达式、属性/数组/列表/关联数组访问、方法调用、关系操作符、赋值、构造函数调用、Bean引用、内联列表和数组、三元运算符和Elvis运算符、变量和用户定义函数、集合选择和投影、模板表达式[11]。

SpEL编译器有三种模式：**OFF**（默认，解释模式）、**IMMEDIATE**（首次评估后编译，失败时抛出异常）、**MIXED**（在解释和编译之间无缝切换）[11]。

**用例**：动态Bean配置、事件监听器过滤（@EventListener带条件）、动态安全访问控制（@PreAuthorize）、动态调度（@Scheduled带SpEL cron）、集合过滤和投影、通过@Value简化配置[11]。

**事件处理**：Spring提供强大的事件处理机制，允许不同组件以松散耦合的方式通信，使用发布-订阅模式。核心组件包括ApplicationEventPublisher（发布事件的接口，ApplicationContext本身实现此接口）、ApplicationListener（处理特定事件类型的接口）、ApplicationEvent（自定义事件的基类，Spring 4.2后任何POJO都可以作为事件）[12]。

内置框架事件：ContextRefreshedEvent、ContextStartedEvent、ContextStoppedEvent、ContextClosedEvent、RequestHandledEvent。

**@EventListener注解**：Spring 4.2开始，@EventListener允许托管Bean的任何公共方法充当监听器，支持使用SpEL表达式进行条件过滤。**@TransactionalEventListener**将事件监听器绑定到事务阶段，如AFTER_COMMIT、AFTER_ROLLBACK、AFTER_COMPLETION、BEFORE_COMMIT[12]。

Spring事件默认是**同步的**——发布者线程阻塞直到所有监听器完成处理。可以通过@Async注解和@EnableAsync或ApplicationEventMulticaster Bean与TaskExecutor实现异步处理[12]。

---

## 第三部分：Spring开发者必备知识

### 3.1 配置类型

**XML配置（传统方式）**：原始Spring配置方法使用XML文件定义和连接依赖。XML配置是传统的声明式方法，Bean（控制器、视图解析器）在XML文件中定义（如web.xml和dispatcher-servlet.xml）。优点：集中配置、易于理解、更改无需重新编译、避免框架入侵代码。缺点：冗长、运行时错误、无编译时类型检查[13]。

**注解配置**：从Spring 3.0开始，注解配置消除了XML文件的需要，简化了配置。核心注解包括`@Component`、`@Service`、`@Repository`、`@Controller`、`@RestController`、`@Configuration`、`@Bean`、`@ComponentScan`和`@Autowired`。Spring Boot的`@SpringBootApplication`包含`@SpringBootConfiguration`、`@EnableAutoConfiguration`和`@ComponentScan`[13]。

**Java配置（@Configuration + @Bean）**：使用Java类注解`@Configuration`并包含`@Bean`方法。提供编译时类型检查，更容易发现错误。支持`@Import`模块化`@Configuration`类，使用`@Profile`和`@Conditional`实现条件配置，结合Java和XML配置（XML-centric或Java-centric）[13]。

**比较总结**：XML配置适用于传统企业项目和库依赖（避免对Spring的耦合）；注解配置适用于新Spring Boot项目，更简洁、更受青睐；Java配置提供编译时类型检查，是Spring Boot应用的标准方式。关键是最重要的是在整个应用中保持一致[13]。

### 3.2 关键注解参考

**核心注解**：
- `@Component`：通用构造型注解，标记Java类为Spring管理的组件
- `@Service`：@Component的特化，用于服务层，提高可读性
- `@Repository`：DAO/仓库层的特化，添加持久化异常翻译
- `@Controller`：MVC控制器的特化，与@RequestMapping配合使用
- `@Bean`：在@Configuration类中声明Bean，用于第三方类或工厂方法
- `@Autowired`：自动注入必需依赖，构造函数注入是现代Spring应用推荐的方法
- `@Qualifier`：当存在多个同类型Bean时消除歧义
- `@Value`：从配置文件注入属性值
- `@Scope`：定义Bean作用域

**Web注解**：
- `@RequestMapping`：在类和方法级别映射HTTP请求到处理器方法
- `@GetMapping`、`@PostMapping`、`@PutMapping`、`@DeleteMapping`：HTTP方法特定快捷方式
- `@RestController`：创建RESTful Web服务，自动返回JSON或XML格式数据，结合@Controller和@ResponseBody
- `@PathVariable`：绑定URI模板变量到方法参数
- `@RequestParam`：绑定查询参数到方法参数
- `@RequestBody`：绑定HTTP请求体到方法参数

**数据注解**：
- `@Transactional`：在服务方法上声明事务边界
- `@Entity`：JPA注解，标记类为数据库实体
- `@Id`：JPA注解，标记主键字段
- `@GeneratedValue`：JPA注解，主键生成策略
- `@Table`：JPA注解，指定表名
- `@Column`：JPA注解，指定列详细信息

**测试注解**：
- `@SpringBootTest`：加载完整应用上下文进行集成测试
- `@WebMvcTest`：仅初始化Web层（@Controller、@ControllerAdvice、Filter）
- `@DataJpaTest`：仅初始化JPA组件（@Entity和Spring Data JPA仓库）
- `@JsonTest`：测试JSON序列化/反序列化
- `@RestClientTest`：测试REST客户端交互
- `@MockBean`：为被注解的Spring Bean创建Mock实现
- `@MockitoBean`（Spring Boot 3.4+）：`@MockBean`的现代替代
- `@ActiveProfiles`：在测试中启用特定Spring Boot Profile

### 3.3 依赖管理

**Maven vs Gradle for Spring项目**：

**Maven**：使用基于XML的配置文件（pom.xml）定义项目结构、依赖和生命周期阶段。优点：简洁、稳定、成熟的生态系统、广泛的插件支持、可靠的依赖管理。缺点：XML冗长、性能限制、刚性。适合传统企业项目和初学者[14]。

**Gradle**：使用基于Groovy或Kotlin的DSL，提供更简洁和表达性的配置语法。优点：增量构建、复合构建、基础设施管理（包装器、自动配置）、构建速度更快。缺点：学习曲线陡峭、插件兼容性问题。适合复杂、多模块或自定义构建，以及大型项目[14]。

关键引用：“Gradle将Spring Boot团队的CI构建时间减少了3-4倍，本地构建时间减少了20-30倍”[14]。

**Spring Boot起步依赖**：Spring Boot通过起步依赖包简化依赖管理。起步依赖分为三类：应用起步依赖（用于构建完整应用，如spring-boot-starter-web）、技术起步依赖（用于添加安全/日志等功能）、生产就绪起步依赖（用于监控和健康检查）。spring-boot-starter-test从2.2.0版本开始包含JUnit 5、Hamcrest和Mockito库[14]。

**Bill of Materials (BOM)与依赖版本管理**：BOM是定义一组相关工件依赖版本的特殊工件。导入BOM有助于管理相关依赖的一致版本。Spring Boot通过spring-boot-starter-parent和spring-boot-dependencies工件使用BOM，定义默认库版本。在Maven中覆盖版本：设置相应属性（如`<activemq.version>5.16.3</activemq.version>`）或在依赖声明中直接指定版本。在Gradle中：使用io.spring.dependency-management插件，导入BOM，设置ext属性（如`ext['activemq.version'] = '5.16.3'`）或直接指定版本。每个Spring Boot版本针对特定第三方依赖集设计和测试，覆盖版本可能导致兼容性问题[14]。

**Spring Boot Maven/Gradle插件能力**：创建可执行JAR（fat JAR）并嵌入服务器、管理依赖版本、提供开发工具。关键命令：`mvn spring-boot:run` / `gradle bootRun`运行应用；`mvn package` / `gradle bootJar`构建可执行fat JAR；`mvn spring-boot:build-image` / `gradle bootBuildImage`使用Cloud Native Buildpacks构建OCI容器镜像[14]。

### 3.4 测试策略

**单元测试（JUnit 5 + Mockito）**：80/20规则：约80%单元测试，20%集成测试。每个测试应验证单一行为。JUnit 5支持Java 8及以上所有现代特性。spring-boot-starter-test从2.2.0版本开始包含JUnit 5、Hamcrest和Mockito库。最佳实践：遵循AAA（Arrange-Act-Assert）、使用描述性测试名称、Mock依赖（而非被测试类）、保持测试独立、使用测试Profile、避免反模式（如过度使用verify或不必要地加载Spring上下文）[15]。

**集成测试（@SpringBootTest）**：@SpringBootTest告诉Spring Boot寻找主配置类并使用它启动Spring应用上下文，加载完整应用上下文进行集成测试。@Transactional将每个测试包装在事务中，回滚更改。测试金字塔推荐：70%单元测试、20%集成测试、10%端到端测试[15]。

**切片测试**：
- **@WebMvcTest**：仅初始化Web层（@Controller、@ControllerAdvice、Filter），使用Spring的MockMvc测试Web层
- **@DataJpaTest**：仅初始化JPA组件（@Entity和Spring Data JPA仓库）
- **@JsonTest**：测试JSON序列化/反序列化
- **@RestClientTest**：测试REST客户端交互

**Testcontainers for数据库测试**：允许对真实生产级数据库（如MySQL in Docker）进行测试，而不是嵌入式H2数据库。推荐使用单例容器模式优化测试执行。Spring Boot 4.0测试更新包括Testcontainers 2.0，模块名称改为testcontainers-前缀（如testcontainers-postgresql），并移除JUnit 4支持[15]。

**REST API测试**：
- **MockMvc**：在不启动实际服务器的情况下执行API调用，代码调用方式与处理HTTP请求完全相同
- **WebTestClient**：响应式，支持Mock和真实服务器环境
- **TestRestTemplate**：使用@SpringBootTest随机端口启动真实服务器测试，在Spring Boot 4中已弃用，替代为RestTestClient
- **RestTestClient**：提供更表达性的API，在Spring Boot 4中需要显式@AutoConfigureRestTestClient注解

Spring Boot 4.0测试更新还包括：JUnit 6作为基础、每个起步依赖对应测试起步依赖的模块化设计、Spring Framework 7中缓存的ApplicationContext自动暂停、更新库版本（Mockito 5.20、HtmlUnit 4.17、Awaitility 4.3.0、AssertJ 3.27.6、Hamcrest 3.0、Selenium 4.37）[15]。

### 3.5 安全基础

**Spring Security核心概念**：
- **认证**：你是谁？验证身份（用户名/密码、JWT、OAuth2）
- **授权**：你被允许做什么？基于角色或权限的访问控制

**安全过滤器链（SecurityFilterChain）**：所有内置过滤器存储在一个Map中，键为类名，值为顺序。第一个过滤器顺序为100，后续每个步长100。"form-login"使Spring Security添加UsernamePasswordAuthenticationFilter来验证用户名和密码。addFilterBefore将自定义过滤器添加到目标过滤器之前（较小顺序），addFilterAt将两个过滤器设置为相同顺序。过滤器链按顺序排序以正确执行[16]。

在Spring Security 6中，SecurityFilterChain Bean是关键概念。安全配置通过声明其中一个Bean定义——无需继承。已弃用的WebSecurityConfigurerAdapter不应再使用[16]。

**OAuth2/OIDC支持**：Spring Security提供全面的OAuth 2.0支持，包括三个主要功能集：OAuth2资源服务器（保护API，支持JWT和透明令牌）、OAuth2客户端（通过OAuth2/OpenID Connect登录用户、访问受保护资源）、OAuth2授权服务器[16]。

OAuth2资源服务器使用JWT时，通过JwtDecoder验证令牌，最小配置只需设置issuer-uri或introspection-uri属性。OAuth2客户端使用oauth2Login()和配置ClientRegistration实现用户登录，使用oauth2Client()和配置OAuth2AuthorizedClientManager访问受保护资源[16]。

Spring Security 6.4版本增加了对RestClient的OAuth2支持，通过OAuth2ClientHttpRequestInterceptor和.attributes()方法传递客户端注册ID[16]。

**方法级安全**：使用@EnableMethodSecurity（Spring Security 6+）启用，替换了@EnableGlobalMethodSecurity。关键注解：@PreAuthorize（方法执行前检查授权，支持SpEL表达式）、@PostAuthorize（方法执行后检查授权）、@Secured（更简单，仅基于角色的授权）[16]。

**CSRF与CORS**：
- **CSRF**：REST API禁用（无状态，无浏览器会话），传统MVC应用启用（基于表单登录）
- **CORS**：通过CorsConfigurationSource Bean或@CrossOrigin注解配置

**常见安全错误**：暴露Actuator端点、使用antMatchers而非requestMatchers、将JWT存储在localStorage、不处理AuthenticationException/AccessDeniedException[16]。

**JWT认证最佳实践**：使用BCryptPasswordEncoder（强度因子12）进行密码哈希、使用jjwt库实现JWT认证、使用httpOnly Cookie存储令牌（比localStorage更安全，后者易受XSS攻击）[16]。

### 3.6 实用知识

**Profile与环境特定配置**：Spring Boot Profile允许将特定Bean和配置属性分组，使其仅在特定环境中加载。Spring Boot先加载公共application.properties，然后加载环境特定的属性文件。设置Profile：`-Dspring.profiles.active=local`、`-Dspring.profiles.active=dev`等。Spring Boot 2.4+支持Profile组，允许激活Profile捆绑包。Profile特定Bean使用@Profile注解创建。最佳实践：绝不硬编码密钥、保持基础配置最小化、按环境分离基础设施配置、使用Profile表示环境而非功能、微服务中使用外部化配置（如Spring Cloud Config、Consul、Kubernetes ConfigMaps）[17]。

**外部化配置**：Spring Boot支持通过多种外部配置源进行配置，包括Java属性文件、YAML文件、环境变量和命令行参数。配置优先级（最高优先）：命令行参数 > JNDI属性 > 系统属性 > 操作系统环境变量 > application-{profile}.properties/.yml > application.properties/.yml > @PropertySource > 默认值。类型安全配置通过@ConfigurationProperties带前缀实现，支持结构化和验证配置绑定[17]。

**日志（SLF4J/Logback）**：Spring Boot内部使用Commons Logging，但底层日志实现开放。默认使用Logback（如果使用起步依赖）。默认日志输出包括日期时间、日志级别、进程ID、线程名、日志名和消息。日志文件在达到10 MB时轮转。可以定义日志组。支持结构化日志的Elastic Common Schema（ECS）、Graylog Extended Log Format（GELF）和Logstash JSON格式[17]。

SLF4J作为抽象层，可以在部署时插入首选日志框架，Logback作为默认实现。Spring Boot推荐使用logback-spring.xml而非默认的logback.xml，因为后者加载过早无法使用扩展。使用springProfile元素可根据活动Profile包含或排除配置部分[17]。

日志最佳实践：使用适当日志级别（TRACE、DEBUG、INFO、WARN、ERROR）、避免记录敏感数据、使用滚动文件追加器、启用异步日志、使用MDC获取上下文信息、生产环境采用结构化日志（JSON）。Lombok的@Slf4j注解是最常用的Spring Boot日志注解[17]。

**Actuator端点**：Spring Boot Actuator为应用带来生产就绪功能。它主要通过HTTP端点或JMX Bean暴露操作信息。关键端点包括：
- `/actuator/health`：应用健康（存活/就绪探针）
- `/actuator/info`：应用信息（构建、Git、自定义）
- `/actuator/metrics`：JVM、HTTP、数据库连接指标
- `/actuator/env`：环境属性（注意：敏感！）
- `/actuator/beans`：上下文中的所有Spring Bean
- `/actuator/loggers`：运行时查看/更改日志级别
- `/actuator/threaddump`：线程转储用于调试
- `/actuator/heapdump`：堆转储用于内存分析（注意：大文件！）
- `/actuator/prometheus`：Prometheus格式指标

安全注意事项：仅暴露所需端点，使用单独管理端口，生产环境必须保护Actuator端点。自定义端点可使用@Endpoint、@ReadOperation、@WriteOperation和@DeleteOperation注解创建。Micrometer提供类似SLF4J的指标抽象，但用于监控系统[17]。

**错误处理与验证**：使用@ControllerAdvice和@ExceptionHandler集中管理异常。@ControllerAdvice适用于MVC应用（可能需要@ResponseBody返回JSON），@RestControllerAdvice自动包含@ResponseBody，适合REST控制器。

最佳实践：为业务逻辑错误创建扩展RuntimeException的自定义异常，使用集中式错误处理，提供有意义的错误消息，使用适当HTTP状态码（404、400、500），避免在生产环境暴露堆栈跟踪，正确记录日志以方便调试[18]。

验证使用Bean Validation（Jakarta Validation）：使用@Valid触发控制器方法参数上的自动验证。常见验证注解包括@NotBlank、@Email、@Size、@NotNull。验证错误可以使用@ExceptionHandler(MethodArgumentNotValidException.class)捕获以返回结构化错误响应。目标是尽可能不在Controller方法中显式处理异常——它们是横切关注点，应单独处理[18]。

---

## 结论

从Java Servlets到Spring Boot的演进历程，是Java Web开发不断追求简化、效率和生产力的体现。每一次技术迭代都源于对前一代技术痛点的深刻反思：CGI的多进程开销推动了Servlets的诞生；Servlets的HTML生成混乱催生了JSP；JSP的嵌入Java代码问题推动了MVC框架的发展；EJB的极端复杂性造就了Spring Framework；而Spring的配置复杂性最终孕育了Spring Boot。

Spring Framework通过依赖注入、面向切面编程、声明式事务管理和MVC架构等核心功能，彻底改变了企业Java开发的方式。Spring Boot在此基础上通过自动配置、起步依赖和嵌入式服务器，将开发效率提升到了新的高度，并成为微服务架构的标准技术栈。

对于现代Java开发者而言，掌握Spring生态系统的核心概念——从IoC容器、AOP、数据访问、事务管理到安全、测试和生产监控——是构建高质量、可维护企业级应用的基础。随着Spring Boot 4.0的模块化演进和GraalVM原生编译支持，Spring生态继续在性能和开发体验上优化，但其核心价值——简化企业Java开发——始终如一。

---

### 来源

[1] Java Servlets: Lifecycle, Performance, and History: https://medium.com/@srisatyabhargavgrandhi/java-servlets-b31e814794d

[2] JSP Technology and Its Evolution: https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/beans.html

[3] EJB 2.x vs EJB 3.x Differences and Improvements: https://www.geeksforgeeks.org/advance-java/aspect-oriented-programming-aop-in-spring-framework

[4] Spring Framework History and Evolution: https://springtutorials.com/spring-framework-history

[5] Spring Boot Official Documentation: https://spring.io/projects/spring-boot

[6] Spring Framework IoC Container and Dependency Injection: https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/beans.html

[7] Spring AOP Documentation: https://docs.spring.io/spring-framework/reference/core/aop.html

[8] Spring MVC Request Processing Pipeline: https://docs.spring.io/spring-framework/docs/4.3.15.RELEASE/spring-framework-reference/html/aop.html

[9] Spring Data JPA and JdbcTemplate Comparison: https://docs.spring.io/spring-framework/reference/core/aop.html

[10] Deep Understanding of @Transactional Annotation: https://bentodev.hashnode.dev/deep-understanding-of-the-transactional-annotation-in-spring-framework

[11] Spring Expression Language (SpEL) Guide: https://docs.spring.io/spring-framework/reference/core/aop.html

[12] Spring Event Handling and Publishing: https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/beans.html

[13] Spring Configuration Types: XML vs Annotation vs Java Config: https://www.geeksforgeeks.org/advance-java/aspect-oriented-programming-aop-in-spring-framework

[14] Maven vs Gradle for Spring Projects: https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/beans.html

[15] Spring Boot Testing Strategies: https://docs.spring.io/spring-framework/reference/core/aop.html

[16] Spring Security Filter Chain and OAuth2 Configuration: https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/beans.html

[17] Spring Boot Externalized Configuration and Actuator: https://spring.io/projects/spring-boot

[18] Spring Boot Error Handling and Validation Best Practices: https://docs.spring.io/spring-framework/reference/core/aop.html
