/**
 * Numerical catalogue schema boundary.
 *
 * These schemas describe source metadata and normalized records. They deliberately
 * contain no Arabic names, transliterations, asterism membership, line geometry, or
 * teaching roles.
 */

export const HIPPARCOS_I311_SOURCE_V1 = {
  catalogueId: 'CDS_I311',
  catalogueTitle: 'Hipparcos, the New Reduction',
  tableId: 'hip2.dat',
  archiveVariant: 'AUTHOR_REPLACEMENT_2008-09-16',
  referenceFrame: 'ICRS',
  referenceEpoch: {
    sourceNotation: 'Ep=1991.25',
    value: 1991.25,
    timeScale: 'UNSPECIFIED_BY_I311_METADATA',
  },
  rightAscensionProperMotion: {
    sourceLabel: 'pmRA',
    sourceSymbol: 'mu_alpha_star',
    normalizedField: 'properMotionRaCosDecMilliarcsecondsPerYear',
    unit: 'mas/yr',
  },
} as const;

export interface HipparcosI311FieldDefinition {
  readonly sourceLabel: string;
  readonly byteRange: string;
  readonly normalizedField: string;
  readonly sourceUnit: string;
  readonly nullable: boolean;
}

/**
 * The exact Phase 1 main-table parser field contract. Source units and byte ranges are
 * transcribed from the official CDS I/311 ReadMe. A source unit of `---` is retained
 * as `SOURCE_UNSPECIFIED`; it is not silently reclassified as dimensionless.
 */
export const HIPPARCOS_I311_MAIN_FIELD_CONTRACT_V1 = [
  {
    sourceLabel: 'HIP',
    byteRange: '1-6',
    normalizedField: 'hipId',
    sourceUnit: 'NONE',
    nullable: false,
  },
  {
    sourceLabel: 'Sn',
    byteRange: '8-10',
    normalizedField: 'newReductionSolutionCode',
    sourceUnit: 'NONE',
    nullable: false,
  },
  {
    sourceLabel: 'So',
    byteRange: '12',
    normalizedField: 'originalReductionSolutionCode',
    sourceUnit: 'NONE',
    nullable: false,
  },
  {
    sourceLabel: 'Nc',
    byteRange: '14',
    normalizedField: 'componentCount',
    sourceUnit: 'NONE',
    nullable: false,
  },
  {
    sourceLabel: 'RArad',
    byteRange: '16-28',
    normalizedField: 'rightAscensionIcrsRadians',
    sourceUnit: 'rad',
    nullable: false,
  },
  {
    sourceLabel: 'DErad',
    byteRange: '30-42',
    normalizedField: 'declinationIcrsRadians',
    sourceUnit: 'rad',
    nullable: false,
  },
  {
    sourceLabel: 'Plx',
    byteRange: '44-50',
    normalizedField: 'parallaxMilliarcseconds',
    sourceUnit: 'mas',
    nullable: false,
  },
  {
    sourceLabel: 'pmRA',
    byteRange: '52-59',
    normalizedField: 'properMotionRaCosDecMilliarcsecondsPerYear',
    sourceUnit: 'mas/yr',
    nullable: false,
  },
  {
    sourceLabel: 'pmDE',
    byteRange: '61-68',
    normalizedField: 'properMotionDecMilliarcsecondsPerYear',
    sourceUnit: 'mas/yr',
    nullable: false,
  },
  {
    sourceLabel: 'e_RArad',
    byteRange: '70-75',
    normalizedField: 'rightAscensionCosDecErrorMilliarcseconds',
    sourceUnit: 'mas',
    nullable: false,
  },
  {
    sourceLabel: 'e_DErad',
    byteRange: '77-82',
    normalizedField: 'declinationErrorMilliarcseconds',
    sourceUnit: 'mas',
    nullable: false,
  },
  {
    sourceLabel: 'e_Plx',
    byteRange: '84-89',
    normalizedField: 'parallaxErrorMilliarcseconds',
    sourceUnit: 'mas',
    nullable: false,
  },
  {
    sourceLabel: 'e_pmRA',
    byteRange: '91-96',
    normalizedField: 'properMotionRaCosDecErrorMilliarcsecondsPerYear',
    sourceUnit: 'mas/yr',
    nullable: false,
  },
  {
    sourceLabel: 'e_pmDE',
    byteRange: '98-103',
    normalizedField: 'properMotionDecErrorMilliarcsecondsPerYear',
    sourceUnit: 'mas/yr',
    nullable: false,
  },
  {
    sourceLabel: 'Ntr',
    byteRange: '105-107',
    normalizedField: 'fieldTransitsUsed',
    sourceUnit: 'NONE',
    nullable: false,
  },
  {
    sourceLabel: 'F2',
    byteRange: '109-113',
    normalizedField: 'goodnessOfFit',
    sourceUnit: 'SOURCE_UNSPECIFIED',
    nullable: false,
  },
  {
    sourceLabel: 'F1',
    byteRange: '115-116',
    normalizedField: 'rejectedDataPercent',
    sourceUnit: 'percent',
    nullable: false,
  },
  {
    sourceLabel: 'var',
    byteRange: '118-123',
    normalizedField: 'cosmicDispersionSourceValue',
    sourceUnit: 'SOURCE_UNSPECIFIED',
    nullable: false,
  },
  {
    sourceLabel: 'ic',
    byteRange: '125-128',
    normalizedField: 'supplementCatalogueEntry',
    sourceUnit: 'NONE',
    nullable: false,
  },
  {
    sourceLabel: 'Hpmag',
    byteRange: '130-136',
    normalizedField: 'hipparcosMagnitude',
    sourceUnit: 'mag',
    nullable: false,
  },
  {
    sourceLabel: 'e_Hpmag',
    byteRange: '138-143',
    normalizedField: 'hipparcosMagnitudeError',
    sourceUnit: 'mag',
    nullable: false,
  },
  {
    sourceLabel: 'sHp',
    byteRange: '145-149',
    normalizedField: 'hipparcosMagnitudeScatter',
    sourceUnit: 'mag',
    nullable: false,
  },
  {
    sourceLabel: 'VA',
    byteRange: '151',
    normalizedField: 'variabilityAnnexReference',
    sourceUnit: 'NONE',
    nullable: false,
  },
  {
    sourceLabel: 'B-V',
    byteRange: '153-158',
    normalizedField: 'bMinusV',
    sourceUnit: 'mag',
    nullable: true,
  },
  {
    sourceLabel: 'e_B-V',
    byteRange: '160-164',
    normalizedField: 'bMinusVError',
    sourceUnit: 'mag',
    nullable: true,
  },
  {
    sourceLabel: 'V-I',
    byteRange: '166-171',
    normalizedField: 'vMinusI',
    sourceUnit: 'mag',
    nullable: true,
  },
  {
    sourceLabel: 'UW',
    byteRange: '172-276',
    normalizedField: 'upperTriangularWeightMatrixSourceValues',
    sourceUnit: 'SOURCE_UNSPECIFIED',
    nullable: false,
  },
] as const satisfies readonly HipparcosI311FieldDefinition[];

export const HIPPARCOS_I311_MAIN_RECORD_SCHEMA_V1 = {
  $schema: 'https://json-schema.org/draft/2020-12/schema',
  $id: 'urn:ufuq:schema:catalogue:hipparcos-i311-main-record:v1',
  title: 'UFUQ normalized CDS I/311 main-table record',
  type: 'object',
  additionalProperties: false,
  required: [
    'hipId',
    'newReductionSolutionCode',
    'solutionFamily',
    'solutionPeculiarityFlags',
    'originalReductionSolutionCode',
    'componentCount',
    'rightAscensionIcrsRadians',
    'declinationIcrsRadians',
    'parallaxMilliarcseconds',
    'properMotionRaCosDecMilliarcsecondsPerYear',
    'properMotionDecMilliarcsecondsPerYear',
    'rightAscensionCosDecErrorMilliarcseconds',
    'declinationErrorMilliarcseconds',
    'parallaxErrorMilliarcseconds',
    'properMotionRaCosDecErrorMilliarcsecondsPerYear',
    'properMotionDecErrorMilliarcsecondsPerYear',
    'fieldTransitsUsed',
    'goodnessOfFit',
    'rejectedDataPercent',
    'cosmicDispersionSourceValue',
    'supplementCatalogueEntry',
    'hipparcosMagnitude',
    'hipparcosMagnitudeError',
    'hipparcosMagnitudeScatter',
    'variabilityAnnexReference',
    'bMinusV',
    'bMinusVError',
    'vMinusI',
    'upperTriangularWeightMatrixSourceValues',
    'supplement',
  ],
  properties: {
    hipId: { type: 'integer', minimum: 1, maximum: 999999 },
    newReductionSolutionCode: { type: 'integer', minimum: 0, maximum: 159 },
    solutionFamily: {
      enum: [
        'NO_NEW_SOLUTION',
        'STOCHASTIC',
        'VIM',
        'FIVE_PARAMETER',
        'SEVEN_PARAMETER',
        'NINE_PARAMETER',
      ],
    },
    solutionPeculiarityFlags: {
      type: 'array',
      uniqueItems: true,
      items: { enum: ['DOUBLE', 'VARIABLE', 'PHOTOCENTRE', 'SECONDARY'] },
    },
    originalReductionSolutionCode: { type: 'integer', minimum: 0, maximum: 5 },
    componentCount: { type: 'integer', minimum: 0, maximum: 9 },
    rightAscensionIcrsRadians: {
      type: 'number',
      minimum: 0,
      exclusiveMaximum: 6.283185307179586,
    },
    declinationIcrsRadians: {
      type: 'number',
      minimum: -1.5707963267948966,
      maximum: 1.5707963267948966,
    },
    parallaxMilliarcseconds: { type: 'number' },
    properMotionRaCosDecMilliarcsecondsPerYear: { type: 'number' },
    properMotionDecMilliarcsecondsPerYear: { type: 'number' },
    rightAscensionCosDecErrorMilliarcseconds: { type: 'number', minimum: 0 },
    declinationErrorMilliarcseconds: { type: 'number', minimum: 0 },
    parallaxErrorMilliarcseconds: { type: 'number', minimum: 0 },
    properMotionRaCosDecErrorMilliarcsecondsPerYear: { type: 'number', minimum: 0 },
    properMotionDecErrorMilliarcsecondsPerYear: { type: 'number', minimum: 0 },
    fieldTransitsUsed: { type: 'integer', minimum: 0 },
    goodnessOfFit: { type: 'number' },
    rejectedDataPercent: { type: 'integer', minimum: 0, maximum: 100 },
    cosmicDispersionSourceValue: { type: 'number' },
    supplementCatalogueEntry: { type: 'integer', minimum: 0 },
    hipparcosMagnitude: { type: 'number' },
    hipparcosMagnitudeError: { type: 'number', minimum: 0 },
    hipparcosMagnitudeScatter: { type: 'number', minimum: 0 },
    variabilityAnnexReference: { type: 'integer', minimum: 0, maximum: 2 },
    bMinusV: { type: ['number', 'null'] },
    bMinusVError: {
      anyOf: [{ type: 'number', minimum: 0 }, { type: 'null' }],
    },
    vMinusI: { type: ['number', 'null'] },
    upperTriangularWeightMatrixSourceValues: {
      type: 'array',
      minItems: 15,
      maxItems: 15,
      items: { type: 'number' },
    },
    supplement: {
      oneOf: [{ type: 'null' }, { $ref: 'urn:ufuq:schema:catalogue:hipparcos-i311-supplement:v1' }],
    },
  },
  allOf: [
    {
      if: {
        properties: { solutionFamily: { const: 'SEVEN_PARAMETER' } },
        required: ['solutionFamily'],
      },
      then: {
        properties: {
          supplement: {
            allOf: [
              { $ref: 'urn:ufuq:schema:catalogue:hipparcos-i311-supplement:v1' },
              {
                type: 'object',
                properties: { kind: { const: 'SEVEN_PARAMETER' } },
                required: ['kind'],
              },
            ],
          },
        },
      },
    },
    {
      if: {
        properties: { solutionFamily: { const: 'NINE_PARAMETER' } },
        required: ['solutionFamily'],
      },
      then: {
        properties: {
          supplement: {
            allOf: [
              { $ref: 'urn:ufuq:schema:catalogue:hipparcos-i311-supplement:v1' },
              {
                type: 'object',
                properties: { kind: { const: 'NINE_PARAMETER' } },
                required: ['kind'],
              },
            ],
          },
        },
      },
    },
    {
      if: {
        properties: { solutionFamily: { const: 'VIM' } },
        required: ['solutionFamily'],
      },
      then: {
        properties: {
          supplement: {
            allOf: [
              { $ref: 'urn:ufuq:schema:catalogue:hipparcos-i311-supplement:v1' },
              {
                type: 'object',
                properties: { kind: { const: 'VIM' } },
                required: ['kind'],
              },
            ],
          },
        },
      },
    },
    {
      if: {
        properties: {
          solutionFamily: {
            enum: ['NO_NEW_SOLUTION', 'STOCHASTIC', 'FIVE_PARAMETER'],
          },
        },
        required: ['solutionFamily'],
      },
      then: {
        properties: { supplement: { type: 'null' } },
      },
    },
  ],
} as const;

export const HIPPARCOS_I311_SUPPLEMENT_SCHEMA_V1 = {
  $schema: 'https://json-schema.org/draft/2020-12/schema',
  $id: 'urn:ufuq:schema:catalogue:hipparcos-i311-supplement:v1',
  title: 'UFUQ normalized CDS I/311 supplementary solution',
  oneOf: [
    {
      type: 'object',
      additionalProperties: false,
      required: [
        'kind',
        'detectionStatistic',
        'accelerationRaCosDecMilliarcsecondsPerYearSquared',
        'accelerationDecMilliarcsecondsPerYearSquared',
        'accelerationRaCosDecErrorMilliarcsecondsPerYearSquared',
        'accelerationDecErrorMilliarcsecondsPerYearSquared',
        'upperTriangularWeightMatrixSourceValues',
      ],
      properties: {
        kind: { const: 'SEVEN_PARAMETER' },
        detectionStatistic: { type: 'number' },
        accelerationRaCosDecMilliarcsecondsPerYearSquared: { type: 'number' },
        accelerationDecMilliarcsecondsPerYearSquared: { type: 'number' },
        accelerationRaCosDecErrorMilliarcsecondsPerYearSquared: {
          type: 'number',
          minimum: 0,
        },
        accelerationDecErrorMilliarcsecondsPerYearSquared: {
          type: 'number',
          minimum: 0,
        },
        upperTriangularWeightMatrixSourceValues: {
          type: 'array',
          minItems: 13,
          maxItems: 13,
          items: { type: 'number' },
        },
      },
    },
    {
      type: 'object',
      additionalProperties: false,
      required: [
        'kind',
        'detectionStatistic',
        'accelerationRaCosDecMilliarcsecondsPerYearSquared',
        'accelerationDecMilliarcsecondsPerYearSquared',
        'accelerationChangeRaCosDecMilliarcsecondsPerYearCubed',
        'accelerationChangeDecMilliarcsecondsPerYearCubed',
        'accelerationRaCosDecErrorMilliarcsecondsPerYearSquared',
        'accelerationDecErrorMilliarcsecondsPerYearSquared',
        'accelerationChangeRaCosDecErrorMilliarcsecondsPerYearCubed',
        'accelerationChangeDecErrorMilliarcsecondsPerYearCubed',
        'upperTriangularWeightMatrixSourceValues',
      ],
      properties: {
        kind: { const: 'NINE_PARAMETER' },
        detectionStatistic: { type: 'number' },
        accelerationRaCosDecMilliarcsecondsPerYearSquared: { type: 'number' },
        accelerationDecMilliarcsecondsPerYearSquared: { type: 'number' },
        accelerationChangeRaCosDecMilliarcsecondsPerYearCubed: { type: 'number' },
        accelerationChangeDecMilliarcsecondsPerYearCubed: { type: 'number' },
        accelerationRaCosDecErrorMilliarcsecondsPerYearSquared: {
          type: 'number',
          minimum: 0,
        },
        accelerationDecErrorMilliarcsecondsPerYearSquared: {
          type: 'number',
          minimum: 0,
        },
        accelerationChangeRaCosDecErrorMilliarcsecondsPerYearCubed: {
          type: 'number',
          minimum: 0,
        },
        accelerationChangeDecErrorMilliarcsecondsPerYearCubed: {
          type: 'number',
          minimum: 0,
        },
        upperTriangularWeightMatrixSourceValues: {
          type: 'array',
          minItems: 30,
          maxItems: 30,
          items: { type: 'number' },
        },
      },
    },
    {
      type: 'object',
      additionalProperties: false,
      required: [
        'kind',
        'detectionStatistic',
        'vimRaCosDecMilliarcseconds',
        'vimDecMilliarcseconds',
        'vimRaCosDecErrorMilliarcseconds',
        'vimDecErrorMilliarcseconds',
        'upperTriangularWeightMatrixSourceValues',
      ],
      properties: {
        kind: { const: 'VIM' },
        detectionStatistic: { type: 'number' },
        vimRaCosDecMilliarcseconds: { type: 'number' },
        vimDecMilliarcseconds: { type: 'number' },
        vimRaCosDecErrorMilliarcseconds: { type: 'number', minimum: 0 },
        vimDecErrorMilliarcseconds: { type: 'number', minimum: 0 },
        upperTriangularWeightMatrixSourceValues: {
          type: 'array',
          minItems: 13,
          maxItems: 13,
          items: { type: 'number' },
        },
      },
    },
  ],
} as const;
