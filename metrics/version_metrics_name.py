from enum import Enum, auto


class DataType(Enum):
    CheckstyleDataType = "checkstyle"
    DesigniteDesignSmellsDataType = "designite_design"
    DesigniteImplementationSmellsDataType = "designite_implementation"
    DesigniteOrganicTypeSmellsDataType = "designite_type_organic"
    DesigniteOrganicMethodSmellsDataType = "designite_method_organic"
    DesigniteTypeMetricsDataType = "designite_type_metrics"
    DesigniteMethodMetricsDataType = "designite_method_metrics"
    SourceMonitorFilesDataType = "source_monitor_files"
    SourceMonitorDataType = "source_monitor"
    CKDataType = "ck"
    MoodDataType = "mood"
    HalsteadDataType = "halstead"
    BuggedDataType = "bugged"


class DataName(Enum):
    # TODO create accessors for each enumeration
    Bugged = auto(), DataType.BuggedDataType.value, "is_buggy"

    ImperativeAbstraction = auto(), DataType.DesigniteDesignSmellsDataType.value, "Imperative Abstraction"
    MultifacetedAbstraction = auto(), DataType.DesigniteDesignSmellsDataType.value, "Multifaceted Abstraction"
    UnnecessaryAbstraction = auto(), DataType.DesigniteDesignSmellsDataType.value, "Unnecessary Abstraction"
    UnutilizedAbstraction = auto(), DataType.DesigniteDesignSmellsDataType.value, "Unutilized Abstraction"
    DeficientEncapsulation = auto(), DataType.DesigniteDesignSmellsDataType.value, "Deficient Encapsulation"
    UnexploitedEncapsulation = auto(), DataType.DesigniteDesignSmellsDataType.value, "Unexploited Encapsulation"
    BrokenModularization = auto(), DataType.DesigniteDesignSmellsDataType.value, "Broken Modularization"
    Cyclic_DependentModularization = auto(), DataType.DesigniteDesignSmellsDataType.value, "Cyclic - Dependent Modularization"
    InsufficientModularization = auto(), DataType.DesigniteDesignSmellsDataType.value, "Insufficient Modularization"
    Hub_likeModularization = auto(), DataType.DesigniteDesignSmellsDataType.value, "Hub - like Modularization"
    BrokenHierarchy = auto(), DataType.DesigniteDesignSmellsDataType.value, "Broken Hierarchy"
    CyclicHierarchy = auto(), DataType.DesigniteDesignSmellsDataType.value, "Cyclic Hierarchy"
    DeepHierarchy = auto(), DataType.DesigniteDesignSmellsDataType.value, "Deep Hierarchy"
    MissingHierarchy = auto(), DataType.DesigniteDesignSmellsDataType.value, "Missing Hierarchy"
    MultipathHierarchy = auto(), DataType.DesigniteDesignSmellsDataType.value, "Multipath Hierarchy"
    RebelliousHierarchy = auto(), DataType.DesigniteDesignSmellsDataType.value, "Rebellious Hierarchy"
    WideHierarchy = auto(), DataType.DesigniteDesignSmellsDataType.value, "Wide Hierarchy"

    AbstractFunctionCallFromConstructor = auto(), DataType.DesigniteImplementationSmellsDataType.value, "Abstract Function Call From Constructor"
    ComplexConditional = auto(), DataType.DesigniteImplementationSmellsDataType.value, "Complex Conditional"
    ComplexMethod = auto(), DataType.DesigniteImplementationSmellsDataType.value, "Complex Method"
    EmptyCatchClause = auto(), DataType.DesigniteImplementationSmellsDataType.value, "Empty catch clause"
    LongIdentifier = auto(), DataType.DesigniteImplementationSmellsDataType.value, "Long Identifier"
    LongMethod_Designite = auto(), DataType.DesigniteImplementationSmellsDataType.value, "Long Method"
    LongParameterList_Designite = auto(), DataType.DesigniteImplementationSmellsDataType.value, "Long Parameter List"
    LongStatement = auto(), DataType.DesigniteImplementationSmellsDataType.value, "Long Statement"
    MagicNumber = auto(), DataType.DesigniteImplementationSmellsDataType.value, "Magic Number"
    MissingDefault = auto(), DataType.DesigniteImplementationSmellsDataType.value, "Missing default"

    GodClass = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "God Class"
    ClassDataShouldBePrivate = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Class Data Should Be Private"
    ComplexClass = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Complex Class"
    LazyClass = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Lazy Class"
    RefusedBequest = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Refused Bequest"
    SpaghettiCode = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Spaghetti Code"
    SpeculativeGenerality = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Speculative Generality"
    DataClass = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Data Class"
    BrainClass = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Brain Class"
    LargeClass = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Large Class"
    SwissArmyKnife = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Swiss Army Knife"
    AntiSingleton = auto(), DataType.DesigniteOrganicTypeSmellsDataType.value, "Anti Singleton"

    FeatureEnvy = auto(), DataType.DesigniteOrganicMethodSmellsDataType.value, "Feature Envy"
    LongMethod_Organic = auto(), DataType.DesigniteOrganicMethodSmellsDataType.value, "Long Method"
    LongParameterList_Organic = auto(), DataType.DesigniteOrganicMethodSmellsDataType.value, "Long Parameter List"
    MessageChain = auto(), DataType.DesigniteOrganicMethodSmellsDataType.value, "Message Chain"
    DispersedCoupling = auto(), DataType.DesigniteOrganicMethodSmellsDataType.value, "Dispersed Coupling"
    IntensiveCoupling = auto(), DataType.DesigniteOrganicMethodSmellsDataType.value, "Intensive Coupling"
    ShotgunSurgery = auto(), DataType.DesigniteOrganicMethodSmellsDataType.value, "Shotgun Surgery"
    BrainMethod = auto(), DataType.DesigniteOrganicMethodSmellsDataType.value, "Brain Method"

    NumberOfFields = auto(), DataType.DesigniteTypeMetricsDataType.value, "NOF"
    NumberOfPublicFields = auto(), DataType.DesigniteTypeMetricsDataType.value, "NOPF"
    NumberOfMethods_Designite = auto(), DataType.DesigniteTypeMetricsDataType.value, "NOM"
    NumberOfPublicMethods_Designite = auto(), DataType.DesigniteTypeMetricsDataType.value, "NOPM"
    LOCClass = auto(), DataType.DesigniteTypeMetricsDataType.value, "LOC"
    WMC_Designite = auto(), DataType.DesigniteTypeMetricsDataType.value, "WMC"
    NumberOfChildren = auto(), DataType.DesigniteTypeMetricsDataType.value, "NC"
    DepthOfInheritance = auto(), DataType.DesigniteTypeMetricsDataType.value, "DIT"
    LCOM = auto(), DataType.DesigniteTypeMetricsDataType.value, "LCOM"
    FANIN = auto(), DataType.DesigniteTypeMetricsDataType.value, "FANIN"
    FANOUT = auto(), DataType.DesigniteTypeMetricsDataType.value, "FANOUT"

    LOCMethod = auto(), DataType.DesigniteMethodMetricsDataType.value, "LOC"
    CyclomaticComplexity_Designite = auto(), DataType.DesigniteMethodMetricsDataType.value, "CC"
    NumberOfParameters_Designite = auto(), DataType.DesigniteMethodMetricsDataType.value, "PC"

    NCSSForThisFile = auto(), DataType.CheckstyleDataType.value, "NCSS_for_this_file"
    NestedIfElseDepth = auto(), DataType.CheckstyleDataType.value, "Nested_if-else_depth"
    BooleanExpressionComplexity = auto(), DataType.CheckstyleDataType.value, "Boolean_expression_complexity"
    CyclomaticComplexity = auto(), DataType.CheckstyleDataType.value, "Cyclomatic_Complexity"
    NCSSForThisMethod = auto(), DataType.CheckstyleDataType.value, "NCSS_for_this_method"
    NPathComplexity = auto(), DataType.CheckstyleDataType.value, "NPath_Complexity"
    ThrowsCount = auto(), DataType.CheckstyleDataType.value, "Throws_count"
    NCSSForThisClass = auto(), DataType.CheckstyleDataType.value, "NCSS_for_this_class"
    NumberOfProtectedMethod = auto(), DataType.CheckstyleDataType.value, "Number_of_protected_methods"
    NumberOfPackageMethod = auto(), DataType.CheckstyleDataType.value, "Number_of_package_methods"
    NumberOfPrivateMethod = auto(), DataType.CheckstyleDataType.value, "Number_of_private_methods"
    ExecutableStatementCount = auto(), DataType.CheckstyleDataType.value, "Executable_statement_count"
    MethodLength = auto(), DataType.CheckstyleDataType.value, "Method_length"
    FileLength = auto(), DataType.CheckstyleDataType.value, "File_length"
    AnonymousInnerClassLength = auto(), DataType.CheckstyleDataType.value, "Anonymous_inner_class_length"
    NumberOfMethods_Checkstyle = auto(), DataType.CheckstyleDataType.value, "Total_number_of_methods"
    NumberOfPublicMethods_Checkstyle = auto(), DataType.CheckstyleDataType.value, "Number_of_public_methods"
    ClassFanOutComplexity = auto(), DataType.CheckstyleDataType.value, "Class_Fan-Out_Complexity"
    NestedTryDepth = auto(), DataType.CheckstyleDataType.value, "Nested_try_depth"
    ClassDataAbstractionCoupling = auto(), DataType.CheckstyleDataType.value, "Class_Data_Abstraction_Coupling"
    NestedForDepth = auto(), DataType.CheckstyleDataType.value, "Nested_for_depth"

    # TODO SourceMonitorColumns - Need windows to do this.value

    IsConstructor = auto(), DataType.CKDataType.value, "constructor"
    CBO = auto(), DataType.CKDataType.value, "cbo"
    WMC_CK = auto(), DataType.CKDataType.value, "wmc"
    RFC = auto(), DataType.CKDataType.value, "rfc"
    LOC = auto(), DataType.CKDataType.value, "loc"
    Returns = auto(), DataType.CKDataType.value, "returns"
    NumberOfVariables = auto(), DataType.CKDataType.value, "variables"
    NumberOfParameters_CK = auto(), DataType.CKDataType.value, "parameters"
    NumberOfLoops = auto(), DataType.CKDataType.value, "loopQty"
    NumberOfComparisons = auto(), DataType.CKDataType.value, "comparisonsQty"
    NumberOfTryCatch = auto(), DataType.CKDataType.value, "tryCatchQty"
    NumberOfParenthesizedExps = auto(), DataType.CKDataType.value, "parenthesizedExpsQty"
    NumberOfStringLiterals = auto(), DataType.CKDataType.value, "stringLiteralsQty"
    NumberOfNumbers = auto(), DataType.CKDataType.value, "numbersQty"
    NumberOfAssignments = auto(), DataType.CKDataType.value, "assignmentsQty"
    NumberOfMathOperations = auto(), DataType.CKDataType.value, "mathOperationsQty"
    MaxNumberOfNestedBlocks = auto(), DataType.CKDataType.value, "maxNestedBlocks"
    NumberOfAnonymousClasses = auto(), DataType.CKDataType.value, "anonymousClassesQty"
    NumberOfInnerClasses = auto(), DataType.CKDataType.value, "innerClassesQty"
    NumberOfLambdas = auto(), DataType.CKDataType.value, "lambdasQty"
    NumberOfUniqueWords = auto(), DataType.CKDataType.value, "uniqueWordsQty"
    NumberOfModifiers = auto(), DataType.CKDataType.value, "modifiers"
    NumberOfLogStatements = auto(), DataType.CKDataType.value, "logStatementsQty"

    NumberOfAncestors = auto(), DataType.MoodDataType.value, "numberOfAncestors"
    NumberOfSubclasses = auto(), DataType.MoodDataType.value, "numberOfSubclasses"
    NumberOfPrivateAttributes = auto(), DataType.MoodDataType.value, "numbeOfPrivateAttributes"
    NumberOfProtectedAttributes = auto(), DataType.MoodDataType.value, "numberOfProtectedAttributes"
    NumberOfPublicAttributes = auto(), DataType.MoodDataType.value, "numberOfPublicAttributes"
    NumberOfAttributes = auto(), DataType.MoodDataType.value, "numberOfAttributes"
    NumberOfCoupledClasses = auto(), DataType.MoodDataType.value, "numberOfCoupledClasses"
    Cohesion = auto(), DataType.MoodDataType.value, "cohesion"
    NumberOfMethods_Mood = auto(), DataType.MoodDataType.value, "numberOfMethods"
    NumberPublicMethods = auto(), DataType.MoodDataType.value, "numberPublicMethods"
    NumberUserDefinedAttributes = auto(), DataType.MoodDataType.value, "numberUserDefinedAttributes"
    NumberOfInheritedMethods = auto(), DataType.MoodDataType.value, "numberOfInheritedMethods"
    NumberOfPolymorphicMethods = auto(), DataType.MoodDataType.value, "numberOfPolymorphicMethods"

    TotalNumberOfOperators = auto(), DataType.HalsteadDataType.value, "getTotalOperatorsCnt"
    NumberOfDistinctOperators = auto(), DataType.HalsteadDataType.value, "getDistinctOperatorsCnt"
    TotalNumberOfOperands = auto(), DataType.HalsteadDataType.value, "getTotalOparandsCnt"
    NumberOfDistinctOperands = auto(), DataType.HalsteadDataType.value, "getDistinctOperandsCnt"
    Length = auto(), DataType.HalsteadDataType.value, "getLength"
    Vocabulary = auto(), DataType.HalsteadDataType.value, "getVocabulary"
    Volume = auto(), DataType.HalsteadDataType.value, "getVolume"
    Difficulty = auto(), DataType.HalsteadDataType.value, "getDifficulty"
    Effort = auto(), DataType.HalsteadDataType.value, "getEffort"
